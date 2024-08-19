import asyncio
import logging
from datetime import datetime
from unittest.mock import patch

import pytest
import pytest_asyncio
import websockets
from ocpp.routing import after, on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.enums import (
    Action,
    AuthorizationStatus,
    ChargePointErrorCode,
    ChargePointStatus,
    RegistrationStatus,
    RemoteStartStopStatus,
)

from ocpp_mqtt_bridge.cs import on_connect

FAKE_TIME_STR = "2021-09-01T00:00:00.000000"

logging.getLogger("ocpp_mqtt_bridge").setLevel(logging.DEBUG)
logging.getLogger("transitions").setLevel(logging.INFO)


@pytest.fixture
def patch_datetime_now():
    with patch("datetime.datetime") as mock_datetime:
        mock_datetime.now.return_value.isoformat.return_value = FAKE_TIME_STR
        yield mock_datetime


@pytest_asyncio.fixture()
async def ws_server():
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


@pytest_asyncio.fixture
async def cp_simulator(ws_server, ws_client):
    async with ChargePointSimulator("dummy", ws_client) as cp:
        yield cp


@pytest.mark.asyncio
async def test_boot(cp_simulator: ChargePointSimulator, patch_datetime_now) -> None:
    request = call.BootNotification(
        charge_point_model="DummyChargePoint",
        charge_point_vendor="Test",
    )
    response: call_result.BootNotification = await cp_simulator.call(request)

    assert response.status == RegistrationStatus.accepted
    assert response.interval == 10
    assert response.current_time == FAKE_TIME_STR


@pytest.mark.asyncio
async def test_heartbeat(
    cp_simulator: ChargePointSimulator, patch_datetime_now
) -> None:
    request = call.Heartbeat()
    response: call_result.Heartbeat = await cp_simulator.call(request)

    assert response.current_time == FAKE_TIME_STR


@pytest.mark.asyncio
async def test_status_notification(
    cp_simulator: ChargePointSimulator, patch_datetime_now
) -> None:
    request = call.StatusNotification(
        1,
        ChargePointErrorCode.no_error,
        ChargePointStatus.preparing,
        datetime.now().isoformat(),
    )
    await cp_simulator.call(request)


@pytest.mark.asyncio
async def test_connected(
    cp_simulator: ChargePointSimulator, patch_datetime_now
) -> None:
    request = call.StatusNotification(
        1,
        ChargePointErrorCode.no_error,
        ChargePointStatus.preparing,
        datetime.now().isoformat(),
    )
    await cp_simulator.call(request)
    await asyncio.wait_for(cp_simulator.got_remote_start.acquire(), 2)


@pytest.mark.asyncio
async def test_start(cp_simulator: ChargePointSimulator, patch_datetime_now) -> None:
    request = call.StartTransaction(
        connector_id=1, id_tag="", meter_start=0, timestamp=datetime.now().isoformat()
    )
    result: call_result.StartTransaction = await cp_simulator.call(request)

    assert result.id_tag_info["status"] == AuthorizationStatus.accepted  # type: ignore[index]


@pytest.mark.asyncio
async def test_connect_and_start(
    cp_simulator: ChargePointSimulator, patch_datetime_now
) -> None:
    request = call.StatusNotification(
        1,
        ChargePointErrorCode.no_error,
        ChargePointStatus.preparing,
        datetime.now().isoformat(),
    )
    await cp_simulator.call(request)
    await asyncio.wait_for(cp_simulator.got_remote_start.acquire(), 2)

    start_request = call.StartTransaction(
        connector_id=1, id_tag="", meter_start=0, timestamp=datetime.now().isoformat()
    )
    result: call_result.StartTransaction = await cp_simulator.call(start_request)
    assert result.id_tag_info["status"] == AuthorizationStatus.accepted  # type: ignore[index]
