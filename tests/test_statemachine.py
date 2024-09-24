from unittest.mock import AsyncMock

import pytest

from ocpp_mqtt_bridge.central_station import CentralStation, states
from ocpp_mqtt_bridge.mqtt import MQTTInterface
from ocpp_mqtt_bridge.ocpp_interface import OCPPInterface


@pytest.fixture()
def model():
    ocpp = AsyncMock(OCPPInterface)
    ocpp.id = "dummy"

    model = CentralStation(ocpp, AsyncMock(MQTTInterface))
    return model


def test_initial(model):
    assert model.state == "unknown"


@pytest.mark.asyncio
async def test_trigger_transaction(model):
    await model.trigger("Preparing")

    assert model.state == "idle"
    model._ocpp.remote_start.assert_called_once()


@pytest.mark.asyncio
async def test_duplicate_events(model):
    await model.trigger("Preparing")
    await model.trigger("Preparing")
    await model.trigger("Preparing")

    assert model.state == "idle"
    model._ocpp.remote_start.assert_called_once()


@pytest.mark.asyncio
async def test_sequence(model):
    await model.trigger("Available")
    await model.trigger("Available")
    await model.trigger("Available")
    assert model.state == "disconnected"

    await model.trigger("Preparing")
    await model.trigger("Preparing")
    await model.trigger("Preparing")
    await model.trigger("Preparing")
    await model.trigger("Preparing")
    assert model.state == "idle"

    await model.trigger("StartTransaction")
    await model.trigger("Charging")
    assert model.state == "charging"

    await model.trigger("Charging")
    await model.trigger("Charging")
    await model.trigger("Charging")
    await model.trigger("Charging")
    assert model.state == "charging"

    await model.trigger("Faulted")
    assert model.state == "faulted"

    await model.trigger("Charging")
    assert model.state == "charging"

    await model.trigger("Finishing")
    await model.trigger("Finishing")
    assert model.state == "ready"

    await model.trigger("Available")
    assert model.state == "disconnected"


@pytest.mark.parametrize(
    "test_event,expected_state",
    [
        ("Available", "disconnected"),
        ("Preparing", "idle"),
        ("Charging", "charging"),
        ("StartTransaction", "ready"),
        ("SuspendedEVSE", "ready"),
        ("SuspendedEV", "ready"),
        ("Finishing", "ready"),
        ("Reserved", "disconnected"),
        ("Unavailable", "disconnected"),
        ("Faulted", "faulted"),
    ],
)
@pytest.mark.parametrize("initial_state", states)
@pytest.mark.asyncio
async def test_transition(initial_state, test_event, expected_state, model):
    model.state = initial_state

    await model.trigger(test_event)
    assert model.state == expected_state
