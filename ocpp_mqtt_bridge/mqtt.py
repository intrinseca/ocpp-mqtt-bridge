import logging
from abc import ABC, abstractmethod
from typing import Any, Generic, Protocol, TypeVar

import aiomqtt
from aiomqtt.types import PayloadType

logger = logging.getLogger(__name__)

T = TypeVar("T", contravariant=True)


class SetHandler(Protocol[T]):
    async def __call__(self, value: T, /) -> None: ...


class Entity:
    def __init__(self, *topic) -> None:
        self.topic = "/".join(topic)
        self.client: aiomqtt.Client | None = None

    async def publish(self, value: Any) -> None:
        if self.client is None:
            raise ValueError("Cannot publish on unregistered entity")
        else:
            await self.client.publish(self.topic, str(value), retain=True)


class Sensor(Entity):
    pass


class SetEntity(Entity, Generic[T], ABC):
    def __init__(self, *topic, set_handler: SetHandler[T]) -> None:
        super().__init__(*topic)
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
