from unittest.mock import AsyncMock, Mock

import pytest
from aiomqtt import Client
from transitions import Machine

from ocpp_mqtt_bridge.cs import MyChargePoint, states, transitions

machine = Machine(states=states, transitions=transitions, initial="unknown")


@pytest.fixture()
def model():
    mock_mqtt_client = AsyncMock(Client)
    model = MyChargePoint("dummy", None, mock_mqtt_client)
    machine.add_model(model)

    model.on_enter_idle = Mock()
    return model


def test_initial(model):
    assert model.state == "unknown"


def test_trigger_transaction(model):
    model.trigger("Preparing")

    assert model.state == "idle"
    model.on_enter_idle.assert_called_once()


def test_duplicate_events(model):
    model.trigger("Preparing")
    model.trigger("Preparing")
    model.trigger("Preparing")

    assert model.state == "idle"
    model.on_enter_idle.assert_called_once()


def test_sequence(model):
    model.trigger("Available")
    model.trigger("Available")
    model.trigger("Available")
    assert model.state == "disconnected"

    model.trigger("Preparing")
    model.trigger("Preparing")
    model.trigger("Preparing")
    model.trigger("Preparing")
    model.trigger("Preparing")
    assert model.state == "idle"

    model.trigger("StartTransaction")
    model.trigger("Charging")
    assert model.state == "active"

    model.trigger("Charging")
    model.trigger("Charging")
    model.trigger("Charging")
    model.trigger("Charging")
    assert model.state == "active"

    model.trigger("Finishing")
    model.trigger("Finishing")
    assert model.state == "active"

    model.trigger("Available")
    assert model.state == "disconnected"
