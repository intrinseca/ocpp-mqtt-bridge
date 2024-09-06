from collections.abc import Callable, Coroutine
from dataclasses import dataclass
from typing import Protocol, TypeAlias


@dataclass
class ChargePointInformation:
    vendor: str
    model: str


@dataclass
class ChargingProfilePoint:
    time: int
    power: float


StatusHandler: TypeAlias = Callable[[str, str], Coroutine[None, None, None]]
BootHandler: TypeAlias = Callable[[ChargePointInformation], Coroutine[None, None, None]]
FloatHandler: TypeAlias = Callable[[float], Coroutine[None, None, None]]


class OCPPInterfaceProtocol(Protocol):
    id: str

    async def set_charge_limit(self, new_limit: float) -> None: ...

    async def read_charging_profile(
        self, duration_seconds: int
    ) -> list[ChargingProfilePoint]: ...

    async def read_meter_values(self) -> None: ...

    async def remote_start(self) -> None: ...

    def set_status_handler(self, handler: StatusHandler) -> None: ...
    def set_boot_handler(self, handler: BootHandler) -> None: ...
    def set_power_handler(self, handler: FloatHandler) -> None: ...
    def set_energy_handler(self, handler: FloatHandler) -> None: ...

    async def start(self) -> None: ...


class MQTTInterfaceProtocol(Protocol):
    async def publish_state(self, state: str) -> None: ...

    async def publish_power(self, power: float) -> None: ...

    async def publish_energy(self, energy: float) -> None: ...

    def set_charging_power_handler(self, handler: FloatHandler) -> None: ...

    async def start(self) -> None: ...
