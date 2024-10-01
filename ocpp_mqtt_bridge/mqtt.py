from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any, Generic, Protocol, TypeVar

import aiomqtt
from aiomqtt.message import Message
from aiomqtt.types import PayloadType

from .typing import BoolHandler, FloatHandler, MQTTInterfaceProtocol

logger = logging.getLogger(__name__)

T = TypeVar("T", contravariant=True)


class SetHandler(Protocol[T]):
    async def __call__(self, value: T, /) -> None: ...


class Entity:
    def __init__(self, parent: HAMQTTClient, *topic: str) -> None:
        self.topic = "/".join(topic)
        self.client = parent

    async def publish(self, value: Any) -> None:
        await self.client.publish(self.topic, str(value), retain=True)


class Sensor(Entity):
    pass


class SetEntity(Entity, Generic[T], ABC):
    def __init__(
        self, parent: HAMQTTClient, *topic: str, set_handler: SetHandler[T]
    ) -> None:
        super().__init__(parent, *topic)
        self.set_topic = self.topic + "/set"
        self.set_handler = set_handler

    @abstractmethod
    async def on_set(self, value: str) -> None:
        raise NotImplementedError()


class Number(SetEntity[int]):
    async def on_set(self, value: str) -> None:
        await self.set_handler(int(float(value)))


SWITCH_MAPPING: dict[str, bool] = {"ON": True, "OFF": False}
SWITCH_REVERSE_MAPPING: dict[bool, str] = {v: k for k, v in SWITCH_MAPPING.items()}


class Switch(SetEntity[bool]):
    async def on_set(self, value: str) -> None:
        value_bool = SWITCH_MAPPING.get(value)

        if value_bool is None:
            raise ValueError("Unknown switch value")

        await self.set_handler(value_bool)

    async def publish(self, value: Any) -> None:
        await self.client.publish(
            self.topic, SWITCH_REVERSE_MAPPING[value], retain=True
        )


class HAMQTTClient:
    def __init__(self, prefix: str, *args: Any, **kwargs: Any) -> None:
        self.prefix = prefix
        self.entities: dict[str, SetEntity[Any]] = {}

        self.mqtt = aiomqtt.Client(
            *args, will=aiomqtt.Will(self.topic("online"), "OFF"), **kwargs
        )

    def make_sensor(self, *topic: str) -> Sensor:
        return Sensor(self, *topic)

    def make_number(self, *topic: str, set_handler: SetHandler[int]) -> Number:
        number = Number(self, *topic, set_handler=set_handler)
        self.entities[number.topic] = number

        return number

    def make_switch(self, *topic: str, set_handler: SetHandler[bool]) -> Switch:
        switch = Switch(self, *topic, set_handler=set_handler)
        self.entities[switch.topic] = switch

        return switch

    def topic(self, *t: str) -> str:
        return "/".join([self.prefix, *t])

    def decode_payload(self, payload: PayloadType) -> str:
        match payload:
            case str(value_str):
                return value_str
            case bytes(value_bytes):
                return value_bytes.decode()
            case float(v) | int(v):
                return str(v)
            case _:
                return ""

    async def connect(self) -> None:
        async with self.mqtt:
            await self.publish("online", "ON")

            for entity in self.entities.values():
                t = self.topic(entity.set_topic)
                logger.debug("Subscribing to %s", t)
                await self.mqtt.subscribe(t)

            async for message in self.mqtt.messages:
                logger.debug(
                    "Recieved mqtt message on %s: %s", message.topic, message.payload
                )

                await self.process_message(message)

    async def process_message(self, message: Message) -> None:
        topic = message.topic.value

        if topic.endswith("/set"):
            topic = topic.removesuffix("/set").removeprefix(self.prefix + "/")

        if (set_entity := self.entities.get(topic)) is not None:
            if isinstance(set_entity, SetEntity):
                await set_entity.on_set(self.decode_payload(message.payload))

    async def publish(self, topic: str, *args: Any, **kwargs: Any) -> None:
        await self.mqtt.publish(self.topic(topic), *args, **kwargs)


class MQTTInterface(MQTTInterfaceProtocol):
    def __init__(self, cp_id: str, mqtt_hostname: str, mqtt_prefix: str) -> None:
        self.id = cp_id

        self.client = HAMQTTClient(
            "/".join([mqtt_prefix, cp_id]), hostname=mqtt_hostname
        )

        self.charging_limit_number = self.client.make_number(
            "charging_limit", set_handler=self.on_set_charging_limit
        )

        self._charging_power_handler: FloatHandler | None = None

        self.default_profile_switch = self.client.make_switch(
            "default_profile", set_handler=self.on_default_profile
        )

        self._default_profile_handler: BoolHandler | None = None

        # self.boot_sensor = Sensor(self.client, "boot")
        # self.heartbeat_sensor = Sensor(self.client, "heartbeat")
        self.connector_status_sensor = self.client.make_sensor("connector_status")
        self.state_sensor = self.client.make_sensor("state")
        self.energy_sensor = self.client.make_sensor("energy_meter")
        self.power_sensor = self.client.make_sensor("power")
        # self.meter_start_sensor = Sensor(self.client, "meter_start")
        # self.meter_stop_sensor = Sensor(self.client, "meter_stop")

    async def start(self) -> None:
        await self.client.connect()

    async def publish_state(self, state: str) -> None:
        await self.state_sensor.publish(state)

    async def publish_connector_status(self, state: str) -> None:
        await self.connector_status_sensor.publish(state)

    async def publish_power(self, power: float) -> None:
        await self.power_sensor.publish(power)

    async def publish_energy(self, energy: float) -> None:
        await self.energy_sensor.publish(energy)

    async def publish_default_profile(self, state: bool) -> None:
        await self.default_profile_switch.publish(state)

    def set_charging_power_handler(self, handler: FloatHandler) -> None:
        self._charging_power_handler = handler

    def set_default_profile_handler(self, handler: BoolHandler) -> None:
        self._default_profile_handler = handler

    async def on_set_charging_limit(self, value: float) -> None:
        if self._charging_power_handler is not None:
            await self._charging_power_handler(value)

            # TODO: Move to a publish from the OCPP interface
            await self.charging_limit_number.publish(value)

    async def on_default_profile(self, value: bool) -> None:
        if self._default_profile_handler is not None:
            await self._default_profile_handler(value)
