import datetime
import logging
from typing import Any
from zoneinfo import ZoneInfo

import websockets
from ocpp.routing import after, on
from ocpp.v16 import ChargePoint as cp
from ocpp.v16 import call, call_result
from ocpp.v16.datatypes import (
    ChargingProfile,
    ChargingSchedule,
    ChargingSchedulePeriod,
    IdTagInfo,
)
from ocpp.v16.enums import (
    Action,
    AuthorizationStatus,
    ChargePointErrorCode,
    ChargePointStatus,
    ChargingProfileKindType,
    ChargingProfilePurposeType,
    ChargingRateUnitType,
    MessageTrigger,
    Reason,
    RecurrencyKind,
    RegistrationStatus,
)

from .typing import (
    BoolHandler,
    BootHandler,
    ChargePointInformation,
    ChargingProfilePoint,
    FloatHandler,
    OCPPInterfaceProtocol,
    StatusHandler,
)
from .util import today_at

logger = logging.getLogger(__name__)


class OCPPInterface(cp, OCPPInterfaceProtocol):
    def __init__(
        self,
        cp_id: str,
        connection: websockets.WebSocketServerProtocol,
        response_timeout: int = 30,
    ) -> None:
        self.logger = logging.getLogger(f"{__name__}.{cp_id}")
        super().__init__(cp_id, connection, response_timeout)

        self._status_handler: StatusHandler | None = None
        self._boot_handler: BootHandler | None = None
        self._power_handler: FloatHandler | None = None
        self._energy_handler: FloatHandler | None = None
        self._default_profile_handler: BoolHandler | None = None

    def set_status_handler(self, handler: StatusHandler) -> None:
        self._status_handler = handler

    def set_boot_handler(self, handler: BootHandler) -> None:
        self._boot_handler = handler

    def set_power_handler(self, handler: FloatHandler) -> None:
        self._power_handler = handler

    def set_energy_handler(self, handler: FloatHandler) -> None:
        self._energy_handler = handler

    def set_default_profile_handler(self, handler: BoolHandler) -> None:
        self._default_profile_handler = handler

    async def set_charge_limit(self, limit: float) -> None:
        result: call_result.SetChargingProfile = await self.call(
            call.SetChargingProfile(
                connector_id=0,
                cs_charging_profiles=ChargingProfile(
                    charging_profile_id=2,
                    stack_level=0,
                    charging_profile_purpose=ChargingProfilePurposeType.tx_default_profile,
                    charging_profile_kind=ChargingProfileKindType.absolute,
                    charging_schedule=ChargingSchedule(
                        ChargingRateUnitType.watts,
                        [
                            ChargingSchedulePeriod(0, limit),
                        ],
                    ),
                ),
            )
        )

        self.logger.debug("Set baseline profile to %d W: %s", limit, result.status)

    async def set_default_profile(self, new_value: bool) -> None:
        if new_value:
            await self.enable_default_profile()
        else:
            await self.disable_default_profile()

    async def read_charging_profile(
        self, duration_seconds: int = 60 * 60 * 24
    ) -> list[ChargingProfilePoint]:
        result: call_result.GetCompositeSchedule = await self.call(
            call.GetCompositeSchedule(
                connector_id=1,
                duration=duration_seconds,
                charging_rate_unit=ChargingRateUnitType.watts,
            )
        )

        self.logger.info(
            "Composite Schedule: %s %r", result.status, result.charging_schedule
        )

        if result.charging_schedule is not None:
            return [
                ChargingProfilePoint(p["start_period"], p["limit"])
                for p in result.charging_schedule["charging_schedule_period"]
            ]
        else:
            raise ValueError("Invalid response")

    async def read_meter_values(self) -> None:
        trigger_result: call_result.TriggerMessage = await self.call(
            call.TriggerMessage(MessageTrigger.meter_values)
        )

        self.logger.debug("Requested meter values: %s", trigger_result.status)

    async def remote_start(self) -> None:
        result: call_result.RemoteStartTransaction = await self.call(
            call.RemoteStartTransaction("noIdTag")
        )
        self.logger.debug("Remote start: %s", result.status)

    @on(Action.boot_notification)
    async def on_boot_notification(
        self, charge_point_vendor: str, charge_point_model: str, **kwargs: Any
    ) -> call_result.BootNotification:
        self.logger.debug(
            "Boot from %s %s",
            charge_point_vendor,
            charge_point_model,
        )

        return call_result.BootNotification(
            current_time=datetime.datetime.now(datetime.UTC).isoformat(),
            interval=10,
            status=RegistrationStatus.accepted,
        )

    @after(Action.BootNotification)
    async def after_boot_notification(
        self, charge_point_vendor: str, charge_point_model: str, **kwargs: Any
    ) -> None:
        if self._boot_handler is not None:
            await self._boot_handler(
                ChargePointInformation(charge_point_vendor, charge_point_model)
            )

        await self.enable_default_profile()

    async def enable_default_profile(self) -> None:
        result: call_result.SetChargingProfile = await self.call(
            call.SetChargingProfile(
                connector_id=0,
                cs_charging_profiles=ChargingProfile(
                    charging_profile_id=1,
                    stack_level=1,
                    charging_profile_purpose=ChargingProfilePurposeType.tx_default_profile,
                    charging_profile_kind=ChargingProfileKindType.recurring,
                    recurrency_kind=RecurrencyKind.daily,
                    charging_schedule=ChargingSchedule(
                        ChargingRateUnitType.watts,
                        [
                            ChargingSchedulePeriod(0, 7200),
                        ],
                        duration=18000,
                        start_schedule=today_at(
                            datetime.time(0, 30, tzinfo=ZoneInfo("Europe/London"))
                        ).isoformat(),
                    ),
                ),
            )
        )

        if self._default_profile_handler:
            await self._default_profile_handler(True)

        self.logger.debug("Charging profile set: %s", result.status)

    async def disable_default_profile(self) -> None:
        result: call_result.ClearChargingProfile = await self.call(
            call.ClearChargingProfile(
                connector_id=0,
                id=1,
                stack_level=1,
                charging_profile_purpose=ChargingProfilePurposeType.tx_default_profile,
            )
        )

        if self._default_profile_handler:
            await self._default_profile_handler(False)

        self.logger.debug("Charging profile cleared: %s", result.status)

    @on(Action.heartbeat)
    async def on_heartbeat(self) -> call_result.Heartbeat:
        self.logger.debug("Heartbeat")

        return call_result.Heartbeat(
            current_time=datetime.datetime.now(datetime.UTC).isoformat(),
        )

    @on(Action.status_notification)
    async def on_status_notification(
        self,
        connector_id: int,
        error_code: ChargePointErrorCode,
        status: ChargePointStatus,
        **kwargs: Any,
    ) -> call_result.StatusNotification:
        self.logger.debug(
            "Status: connector %d %s %s",
            connector_id,
            error_code,
            status,
        )

        return call_result.StatusNotification()

    @after(Action.status_notification)
    async def after_status_notification(
        self,
        connector_id: int,
        error_code: ChargePointErrorCode,
        status: ChargePointStatus,
        **kwargs: Any,
    ) -> None:
        if self._status_handler is not None:
            await self._status_handler(str(error_code), str(status))

    @on(Action.start_transaction)
    async def on_start_transaction(
        self,
        connector_id: int,
        id_tag: str,
        meter_start: int,
        timestamp: str,
        reservation_id: int | None = None,
        **kwargs: Any,
    ) -> call_result.StartTransaction:
        self.logger.debug("Transaction started")

        return call_result.StartTransaction(
            1, id_tag_info=IdTagInfo(AuthorizationStatus.accepted)
        )

    @on(Action.stop_transaction)
    async def on_stop_transaction(
        self,
        meter_stop: int,
        timestamp: str,
        transaction_id: int,
        reason: Reason = Reason.local,
        **kwargs: Any,
    ) -> call_result.StopTransaction:
        self.logger.debug("Transaction stopped: %s", reason)

        return call_result.StopTransaction()

    @on(Action.meter_values)
    async def on_meter_values(
        self, connector_id: str, meter_value: list[dict[str, Any]], **kwargs: Any
    ) -> call_result.MeterValues:
        self.logger.debug("Meter Values: %r", meter_value)
        return call_result.MeterValues()

    @after(Action.meter_values)
    async def after_meter_values(
        self, connector_id: str, meter_value: list[dict[str, Any]], **kwargs: Any
    ) -> None:
        latest_sample = max(meter_value, key=lambda m: m["timestamp"])

        for value in latest_sample["sampled_value"]:
            if (
                value["measurand"] == "Energy.Active.Import.Register"
                and self._energy_handler is not None
            ):
                await self._energy_handler(float(value["value"]))
            elif (
                value["measurand"] == "Power.Active.Import"
                and self._power_handler is not None
            ):
                await self._power_handler(float(value["value"]))
