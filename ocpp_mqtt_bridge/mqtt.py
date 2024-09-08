from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from typing import Any, Generic, Protocol, TypeVar

import aiomqtt
from aiomqtt.types import PayloadType

from .typing import FloatHandler, MQTTInterfaceProtocol

logger = logging.getLogger(__name__)

T = TypeVar("T", contravariant=True)


class SetHandler(Protocol[T]):
    async def __call__(self, value: T, /) -> None: ...


class Entity:
    def __init__(self, parent: HAMQTTClient, *topic) -> None:
        self.topic = "/".join([parent.prefix, *topic])
        self.client = parent

    async def publish(self, value: Any) -> None:
        await self.client.publish(self.topic, str(value), retain=True)


class Sensor(Entity):
    pass


class SetEntity(Entity, Generic[T], ABC):
    def __init__(
        self, parent: HAMQTTClient, *topic, set_handler: SetHandler[T]
    ) -> None:
        super().__init__(parent, *topic)
        self.set_topic = self.topic + "/set"
        self.set_handler = set_handler

    @abstractmethod
    async def on_set(self, value: str):
        raise NotImplementedError()


class Number(SetEntity[int]):
    async def on_set(self, value: str):
        await self.set_handler(int(float(value)))


class HAMQTTClient(aiomqtt.Client):
    def __init__(self, prefix, *args, **kwargs) -> None:
        self.prefix = prefix
        self.entities: dict[str, Entity] = {}

        super().__init__(
            *args, will=aiomqtt.Will(self.topic("online"), "OFF"), **kwargs
        )

    def topic(self, *t: str) -> str:
        return "/".join([self.prefix, *t])

    async def register(self, entity: Entity) -> None:
        self.entities[entity.topic] = entity

        if isinstance(entity, SetEntity):
            t = self.topic(entity.set_topic)
            logger.debug("Subscribing to %s", t)
            await self.subscribe(t)

        entity.client = self

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
        async with self:
            await self.publish("online", "ON")

            async for message in self.messages:
                logger.debug(
                    "Recieved mqtt message on %s: %s", message.topic, message.payload
                )

                topic = message.topic.value

                if topic.endswith("/set"):
                    topic = topic.removesuffix("/set").removeprefix(self.prefix + "/")

                if (set_entity := self.entities.get(topic)) is not None:
                    if isinstance(set_entity, SetEntity):
                        await set_entity.on_set(self.decode_payload(message.payload))

    async def publish(self, topic: str, *args, **kwargs) -> None:
        await super().publish(self.topic(topic), *args, **kwargs)


class MQTTInterface(MQTTInterfaceProtocol):
    def __init__(self, cp_id: str, mqtt_hostname: str, mqtt_prefix: str) -> None:
        self.id = cp_id

        self.client = HAMQTTClient(
            "/".join([mqtt_prefix, cp_id]), hostname=mqtt_hostname
        )

        self.charging_limit_number = Number(
            self.client, "charging_limit", set_handler=self.on_set_charging_limit
        )

        self._charging_power_handler: FloatHandler | None = None

        # self.boot_sensor = Sensor(self.client, "boot")
        # self.heartbeat_sensor = Sensor(self.client, "heartbeat")
        # self.connector_status_sensor = Sensor(self.client, "connector_status")
        self.state_sensor = Sensor(self.client, "state")
        self.energy_sensor = Sensor(self.client, "energy_meter")
        self.power_sensor = Sensor(self.client, "power")
        # self.meter_start_sensor = Sensor(self.client, "meter_start")
        # self.meter_stop_sensor = Sensor(self.client, "meter_stop")

    async def start(self) -> None:
        await self.client.connect()

    async def publish_state(self, state: str) -> None:
        await self.state_sensor.publish(state)

    async def publish_power(self, power: float) -> None:
        await self.power_sensor.publish(power)

    async def publish_energy(self, energy: float) -> None:
        await self.energy_sensor.publish(energy)

    def set_charging_power_handler(self, handler: FloatHandler) -> None:
        self._charging_power_handler = handler

    async def on_set_charging_limit(self, value: float) -> None:
        if self._charging_power_handler is not None:
            await self._charging_power_handler(value)
