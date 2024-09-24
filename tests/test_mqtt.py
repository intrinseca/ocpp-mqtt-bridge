from unittest.mock import patch

import aiomqtt
import pytest

from ocpp_mqtt_bridge.mqtt import HAMQTTClient, MQTTInterface


@pytest.fixture()
@patch("aiomqtt.Client", spec=aiomqtt.Client)
def interface(MockClient):
    interface = MQTTInterface("DUMMY", "mqtt.example.com", "ocpp_test")
    return interface


@patch("aiomqtt.Client")
def test_topic(MockClient):
    client = HAMQTTClient("ocpp_test/DUMMY", hostname="mqtt.example.com")
    assert client.topic("TEST") == "ocpp_test/DUMMY/TEST"


@patch("aiomqtt.Client", spec=aiomqtt.Client)
@pytest.mark.asyncio
async def test_publish(MockClient):
    client = HAMQTTClient("ocpp_test/DUMMY", hostname="mqtt.example.com")

    await client.publish("TEST", "value")

    client.mqtt.publish.assert_called_once_with("ocpp_test/DUMMY/TEST", "value")


@pytest.mark.asyncio
async def test_state(interface: MQTTInterface):
    await interface.publish_state("ready")
    interface.client.mqtt.publish.assert_called_once_with(
        "ocpp_test/DUMMY/state", "ready", retain=True
    )
