from unittest.mock import AsyncMock, Mock

import pytest
from transitions.extensions import AsyncMachine as Machine

from ocpp_mqtt_bridge.mqtt import HAMQTTClient
from ocpp_mqtt_bridge.ocpp_interface import OCPPInterface, states, transitions

machine = Machine(states=states, transitions=transitions, initial="unknown")


@pytest.fixture()
def model():
    mock_mqtt_client = AsyncMock(HAMQTTClient)

    model = OCPPInterface("dummy", None, mock_mqtt_client)
    machine.add_model(model)

    model.on_enter_idle = Mock()
    model.on_exit_charging = Mock()
    return model


def test_initial(model):
    assert model.state == "unknown"


@pytest.mark.asyncio
async def test_trigger_transaction(model):
    await model.trigger("Preparing")

    assert model.state == "idle"
    model.on_enter_idle.assert_called_once()


@pytest.mark.asyncio
async def test_duplicate_events(model):
    await model.trigger("Preparing")
    await model.trigger("Preparing")
    await model.trigger("Preparing")

    assert model.state == "idle"
    model.on_enter_idle.assert_called_once()


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
