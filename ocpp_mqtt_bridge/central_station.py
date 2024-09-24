import asyncio
import logging

from ocpp.v16.enums import ChargePointErrorCode
from transitions.extensions import AsyncMachine

from .typing import ChargePointInformation, MQTTInterfaceProtocol, OCPPInterfaceProtocol

states = ["unknown", "disconnected", "idle", "ready", "charging", "faulted"]
transitions = [
    ["Available", ["unknown", "idle", "ready", "faulted", "charging"], "disconnected"],
    ["Available", "disconnected", None],
    ["Reserved", ["unknown", "idle", "ready", "faulted", "charging"], "disconnected"],
    ["Reserved", "disconnected", None],
    [
        "Unavailable",
        ["unknown", "idle", "ready", "faulted", "charging"],
        "disconnected",
    ],
    ["Unavailable", "disconnected", None],
    ["Preparing", ["unknown", "disconnected", "ready", "faulted", "charging"], "idle"],
    ["Preparing", "idle", None],
    [
        "StartTransaction",
        ["unknown", "disconnected", "idle", "faulted", "charging"],
        "ready",
    ],
    ["StartTransaction", "ready", None],
    ["Charging", ["unknown", "disconnected", "idle", "ready", "faulted"], "charging"],
    ["Charging", "charging", None],
    [
        "SuspendedEVSE",
        ["unknown", "disconnected", "idle", "faulted", "charging"],
        "ready",
    ],
    ["SuspendedEVSE", "ready", None],
    [
        "SuspendedEV",
        ["unknown", "disconnected", "idle", "faulted", "charging"],
        "ready",
    ],
    ["SuspendedEV", "ready", None],
    ["Finishing", ["unknown", "disconnected", "idle", "faulted", "charging"], "ready"],
    ["Finishing", "ready", None],
    ["Faulted", ["unknown", "disconnected", "idle", "ready", "charging"], "faulted"],
    ["Faulted", "faulted", None],
]


class CentralStation:
    state: str

    def __init__(
        self,
        ocpp_interface: OCPPInterfaceProtocol,
        mqtt_interface: MQTTInterfaceProtocol,
    ):
        self._ocpp = ocpp_interface
        self._mqtt = mqtt_interface

        self.logger = logging.getLogger(f"{__name__}.{self._ocpp.id}")

        self._ocpp.set_status_handler(self.handle_status)
        self._ocpp.set_boot_handler(self.handle_boot)
        self._ocpp.set_energy_handler(self._mqtt.publish_energy)
        self._ocpp.set_power_handler(self._mqtt.publish_power)

        self._mqtt.set_charging_power_handler(self._ocpp.set_charge_limit)

        self.error_code: str = str(ChargePointErrorCode.no_error)

        self.machine = AsyncMachine(
            model=self,
            states=states,
            transitions=transitions,
            initial="unknown",
            after_state_change="on_state_change",
            model_override=False,
        )

    async def handle_status(self, error_code: str, connector_status: str) -> None:
        self.error_code = error_code
        await self.trigger(connector_status)  # type: ignore[attr-defined]

    async def handle_boot(self, cp_info: ChargePointInformation) -> None:
        pass

    async def on_state_change(self) -> None:
        await self._mqtt.publish_state(self.state)

    async def on_enter_idle(self) -> None:
        await self._ocpp.remote_start()

    async def on_enter_faulted(self) -> None:
        self.logger.error("Fault Detected: %s", self.error_code)

    async def on_exit_charging(self) -> None:
        self.logger.debug("Charge stopped, zeroing power sensor")
        await self._mqtt.publish_power(0)

    async def start(self) -> None:
        await asyncio.gather(self._ocpp.start(), self._mqtt.start())
