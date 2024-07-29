import asyncio
from unittest.mock import patch

import pytest
import pytest_asyncio
import websockets
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.enums import RegistrationStatus

from ocpp_mqtt_bridge.cs import on_connect

FAKE_TIME_STR = "2021-09-01T00:00:00.000000"


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
