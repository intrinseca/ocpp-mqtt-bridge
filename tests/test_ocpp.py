import asyncio
import datetime
import logging
from unittest.mock import AsyncMock

import pytest
import pytest_asyncio
import websockets
from ocpp.routing import after, on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.datatypes import MeterValue, SampledValue
from ocpp.v16.enums import (
    Action,
    AuthorizationStatus,
    ChargePointErrorCode,
    ChargePointStatus,
    ChargingProfileStatus,
    Measurand,
    RegistrationStatus,
    RemoteStartStopStatus,
)

from ocpp_mqtt_bridge.ocpp_interface import OCPPInterface
from ocpp_mqtt_bridge.typing import ChargePointInformation

logging.getLogger("ocpp_mqtt_bridge").setLevel(logging.DEBUG)
logging.getLogger("transitions").setLevel(logging.INFO)


@pytest.fixture
def connection_registry() -> dict[str, OCPPInterface]:
    return {}


@pytest_asyncio.fixture
async def ws_server(connection_registry):
    async def on_connect(
        websocket: websockets.WebSocketServerProtocol,
    ):
        charge_point_id = websocket.path.strip("/").split("/")[-1]

        ocpp = OCPPInterface(charge_point_id, websocket)

        ocpp._boot_handler = AsyncMock()
        ocpp._status_handler = AsyncMock()
        ocpp._boot_handler = AsyncMock()
        ocpp._power_handler = AsyncMock()
        ocpp._energy_handler = AsyncMock()

        connection_registry[charge_point_id] = ocpp

        try:
            await ocpp.start()
        except websockets.exceptions.ConnectionClosedOK:
            pass

    async with websockets.serve(
        on_connect, "127.0.0.1", 9000, subprotocols=["ocpp1.6"]
    ):
        yield


@pytest_asyncio.fixture
async def ws_client():
    async with websockets.connect(
        "ws://localhost:9000/dummy",
        subprotocols=["ocpp1.6"],
    ) as ws:
        yield ws


class ChargePointSimulator(cp):
    def __init__(self, *args, **kwargs):
        self.got_remote_start = asyncio.Semaphore(value=0)
        self.got_charging_profile = asyncio.Semaphore(value=0)
        super().__init__(*args, **kwargs)

    async def send_heartbeat(self, arguments):
        request = call.Heartbeat()
        return self.call(request)

    async def __aenter__(self):
        self.start_task = asyncio.ensure_future(
            self.start(), loop=asyncio.get_running_loop()
        )

        return self

    async def __aexit__(self, exc_type, exc, tb):
        self.start_task.cancel()

    @on(Action.remote_start_transaction)
    async def on_remote_start(self, id_tag: str, **kwargs):
        return call_result.RemoteStartTransaction(RemoteStartStopStatus.accepted)

    @after(Action.remote_start_transaction)
    async def after_remote_start(self, id_tag: str, **kwargs):
        self.got_remote_start.release()

    @on(Action.set_charging_profile)
    async def on_set_charging_profile(
        self, connector_id, cs_charging_profiles, **kwargs
    ):
        return call_result.SetChargingProfile(ChargingProfileStatus.accepted)

    @after(Action.set_charging_profile)
    async def after_charging_profile(
        self, connector_id, cs_charging_profiles, **kwargs
    ):
        self.charging_profile = cs_charging_profiles
        self.got_charging_profile.release()


@pytest_asyncio.fixture
async def cp_simulator(ws_server, ws_client):
    async with ChargePointSimulator("dummy", ws_client) as cp:
        # request = call.BootNotification(
        #     charge_point_model="DummyChargePoint",
        #     charge_point_vendor="Test",
        # )

        # await cp.call(request)

        yield cp


@pytest.mark.asyncio
async def test_id(cp_simulator: ChargePointSimulator, connection_registry) -> None:
    assert connection_registry["dummy"].id == "dummy"


@pytest.mark.asyncio
async def test_boot(
    cp_simulator: ChargePointSimulator, patch_datetime_now, connection_registry
) -> None:
    request = call.BootNotification(
        charge_point_model="DummyChargePoint",
        charge_point_vendor="Test",
    )
    response: call_result.BootNotification = await cp_simulator.call(request)

    assert response.status == RegistrationStatus.accepted
    assert response.interval == 10
    assert response.current_time == datetime.datetime.now(datetime.UTC).isoformat()

    await asyncio.sleep(0.1)  # allow @after handlers to be called

    connection_registry["dummy"]._boot_handler.assert_called_once_with(
        ChargePointInformation("Test", "DummyChargePoint")
    )


@pytest.mark.asyncio
async def test_heartbeat(
    cp_simulator: ChargePointSimulator, patch_datetime_now
) -> None:
    request = call.Heartbeat()
    response: call_result.Heartbeat = await cp_simulator.call(request)

    assert response.current_time == datetime.datetime.now(datetime.UTC).isoformat()


@pytest.mark.asyncio
async def test_status_notification(
    cp_simulator: ChargePointSimulator, patch_datetime_now, connection_registry
) -> None:
    request = call.StatusNotification(
        1,
        ChargePointErrorCode.no_error,
        ChargePointStatus.preparing,
        datetime.datetime.now().isoformat(),
    )
    await cp_simulator.call(request)

    await asyncio.sleep(0.1)  # allow @after handlers to be called

    connection_registry["dummy"]._status_handler.assert_called_once_with(
        "NoError", "Preparing"
    )


@pytest.mark.asyncio
async def test_start(cp_simulator: ChargePointSimulator, patch_datetime_now) -> None:
    request = call.StartTransaction(
        connector_id=1,
        id_tag="",
        meter_start=0,
        timestamp=datetime.datetime.now().isoformat(),
    )
    result: call_result.StartTransaction = await cp_simulator.call(request)

    assert result.id_tag_info["status"] == AuthorizationStatus.accepted  # type: ignore[index]


@pytest.mark.asyncio
async def test_metervalues(
    cp_simulator: ChargePointSimulator, patch_datetime_now, connection_registry
) -> None:
    request = call.MeterValues(
        connector_id=1,
        meter_value=[
            MeterValue(
                timestamp=datetime.datetime.now().isoformat(),
                sampled_value=[
                    SampledValue(
                        value="1000", measurand=Measurand.power_active_import, unit="W"
                    ),
                    SampledValue(
                        value="10000",
                        measurand=Measurand.energy_active_import_register,
                        unit="Wh",
                    ),
                ],
            )
        ],
    )
    result: call_result.MeterValues = await cp_simulator.call(request)

    assert result is not None

    await asyncio.sleep(0.1)  # allow @after handlers to be called

    connection_registry["dummy"]._energy_handler.assert_called_once_with(10000)
    connection_registry["dummy"]._power_handler.assert_called_once_with(1000)


@pytest.mark.asyncio
async def test_connect_and_profile(
    cp_simulator: ChargePointSimulator, patch_datetime_now
) -> None:
    request = call.BootNotification(
        charge_point_model="DummyChargePoint",
        charge_point_vendor="Test",
    )
    await cp_simulator.call(request)

    await asyncio.wait_for(cp_simulator.got_charging_profile.acquire(), 1)

    assert (
        cp_simulator.charging_profile["charging_schedule"]["start_schedule"]
        == "2024-01-02T00:30:00+00:00"
    )

    assert cp_simulator.charging_profile["charging_schedule"]["duration"] == 60 * 60 * 5
