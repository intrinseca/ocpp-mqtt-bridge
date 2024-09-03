import asyncio
import logging

from ocpp.v16.enums import ChargePointErrorCode
from transitions.extensions import AsyncMachine

from .typing import ChargePointInformation, MQTTInterfaceProtocol, OCPPInterfaceProtocol

states = ["unknown", "disconnected", "idle", "ready", "charging", "faulted"]
transitions = [
    ["Available", ["unknown", "idle", "ready", "faulted", "charging"], "disconnected"],
    ["Available", "disconnected", None],
    ["Preparing", ["unknown", "disconnected", "ready", "faulted", "charging"], "idle"],
    ["Preparing", "idle", None],
    [
        "StartTransaction",
        ["unknown", "disconnected", "idle", "faulted", "charging"],
        "ready",
    ],
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

default_machine = AsyncMachine(
    states=states,
    transitions=transitions,
    initial="unknown",
    after_state_change="on_state_change",
    model_override=True,
)


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

        self.error_code = ChargePointErrorCode.no_error

        default_machine.add_model(self)

    async def handle_status(self, error_code, connector_status):
        self.error_code = error_code
        await self.trigger(connector_status)

    async def handle_boot(self, cp_info: ChargePointInformation):
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
