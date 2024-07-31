from dataclasses import dataclass
from ocpp.v16.enums import AvailabilityType as AvailabilityType, CertificateUse as CertificateUse, ChargePointErrorCode as ChargePointErrorCode, ChargePointStatus as ChargePointStatus, ChargingProfilePurposeType as ChargingProfilePurposeType, ChargingRateUnitType as ChargingRateUnitType, DiagnosticsStatus as DiagnosticsStatus, FirmwareStatus as FirmwareStatus, Log as Log, MessageTrigger as MessageTrigger, Reason as Reason, ResetType as ResetType, UpdateType as UpdateType, UploadLogStatus as UploadLogStatus

@dataclass
class CancelReservation:
    reservation_id: int
    def __init__(self, reservation_id) -> None: ...

@dataclass
class CertificateSigned:
    certificate_chain: str
    def __init__(self, certificate_chain) -> None: ...

@dataclass
class ChangeAvailability:
    connector_id: int
    type: AvailabilityType
    def __init__(self, connector_id, type) -> None: ...

@dataclass
class ChangeConfiguration:
    key: str
    value: str
    def __init__(self, key, value) -> None: ...

@dataclass
class ClearCache: ...

@dataclass
class ClearChargingProfile:
    id: int | None = ...
    connector_id: int | None = ...
    charging_profile_purpose: ChargingProfilePurposeType | None = ...
    stack_level: int | None = ...
    def __init__(self, id=..., connector_id=..., charging_profile_purpose=..., stack_level=...) -> None: ...

@dataclass
class DeleteCertificate:
    certificate_hash_data: dict
    def __init__(self, certificate_hash_data) -> None: ...

@dataclass
class ExtendedTriggerMessage:
    requested_message: MessageTrigger
    connector_id: int | None = ...
    def __init__(self, requested_message, connector_id=...) -> None: ...

@dataclass
class GetCompositeSchedule:
    connector_id: int
    duration: int
    charging_rate_unit: ChargingRateUnitType | None = ...
    def __init__(self, connector_id, duration, charging_rate_unit=...) -> None: ...

@dataclass
class GetConfiguration:
    key: list | None = ...
    def __init__(self, key=...) -> None: ...

@dataclass
class GetDiagnostics:
    location: str
    retries: int | None = ...
    retry_interval: int | None = ...
    start_time: str | None = ...
    stop_time: str | None = ...
    def __init__(self, location, retries=..., retry_interval=..., start_time=..., stop_time=...) -> None: ...

@dataclass
class GetInstalledCertificateIds:
    certificate_type: CertificateUse
    def __init__(self, certificate_type) -> None: ...

@dataclass
class GetLocalListVersion: ...

@dataclass
class GetLog:
    log: dict
    log_type: Log
    request_id: int
    retries: int | None = ...
    retry_interval: int | None = ...
    def __init__(self, log, log_type, request_id, retries=..., retry_interval=...) -> None: ...

@dataclass
class InstallCertificate:
    certificate_type: CertificateUse
    certificate: str
    def __init__(self, certificate_type, certificate) -> None: ...

@dataclass
class RemoteStartTransaction:
    id_tag: str
    connector_id: int | None = ...
    charging_profile: dict | None = ...
    def __init__(self, id_tag, connector_id=..., charging_profile=...) -> None: ...

@dataclass
class RemoteStopTransaction:
    transaction_id: int
    def __init__(self, transaction_id) -> None: ...

@dataclass
class ReserveNow:
    connector_id: int
    expiry_date: str
    id_tag: str
    reservation_id: int
    parent_id_tag: str | None = ...
    def __init__(self, connector_id, expiry_date, id_tag, reservation_id, parent_id_tag=...) -> None: ...

@dataclass
class Reset:
    type: ResetType
    def __init__(self, type) -> None: ...

@dataclass
class SendLocalList:
    list_version: int
    update_type: UpdateType
    local_authorization_list: list = ...
    def __init__(self, list_version, update_type, local_authorization_list=...) -> None: ...

@dataclass
class SetChargingProfile:
    connector_id: int
    cs_charging_profiles: dict
    def __init__(self, connector_id, cs_charging_profiles) -> None: ...

@dataclass
class SignedUpdateFirmware:
    request_id: int
    firmware: dict
    retries: int | None = ...
    retry_interval: int | None = ...
    def __init__(self, request_id, firmware, retries=..., retry_interval=...) -> None: ...

@dataclass
class TriggerMessage:
    requested_message: MessageTrigger
    connector_id: int | None = ...
    def __init__(self, requested_message, connector_id=...) -> None: ...

@dataclass
class UnlockConnector:
    connector_id: int
    def __init__(self, connector_id) -> None: ...

@dataclass
class UpdateFirmware:
    location: str
    retrieve_date: str
    retries: int | None = ...
    retry_interval: int | None = ...
    def __init__(self, location, retrieve_date, retries=..., retry_interval=...) -> None: ...

@dataclass
class Authorize:
    id_tag: str
    def __init__(self, id_tag) -> None: ...

@dataclass
class BootNotification:
    charge_point_model: str
    charge_point_vendor: str
    charge_box_serial_number: str | None = ...
    charge_point_serial_number: str | None = ...
    firmware_version: str | None = ...
    iccid: str | None = ...
    imsi: str | None = ...
    meter_serial_number: str | None = ...
    meter_type: str | None = ...
    def __init__(self, charge_point_model, charge_point_vendor, charge_box_serial_number=..., charge_point_serial_number=..., firmware_version=..., iccid=..., imsi=..., meter_serial_number=..., meter_type=...) -> None: ...

@dataclass
class DiagnosticsStatusNotification:
    status: DiagnosticsStatus
    def __init__(self, status) -> None: ...

@dataclass
class FirmwareStatusNotification:
    status: FirmwareStatus
    def __init__(self, status) -> None: ...

@dataclass
class Heartbeat: ...

@dataclass
class LogStatusNotification:
    status: UploadLogStatus
    request_id: int
    def __init__(self, status, request_id) -> None: ...

@dataclass
class MeterValues:
    connector_id: int
    meter_value: list = ...
    transaction_id: int | None = ...
    def __init__(self, connector_id, meter_value=..., transaction_id=...) -> None: ...

@dataclass
class SecurityEventNotification:
    type: str
    timestamp: str
    tech_info: str | None
    def __init__(self, type, timestamp, tech_info) -> None: ...

@dataclass
class SignCertificate:
    csr: str
    def __init__(self, csr) -> None: ...

@dataclass
class SignedFirmwareStatusNotification:
    status: FirmwareStatus
    request_id: int
    def __init__(self, status, request_id) -> None: ...

@dataclass
class StartTransaction:
    connector_id: int
    id_tag: str
    meter_start: int
    timestamp: str
    reservation_id: int | None = ...
    def __init__(self, connector_id, id_tag, meter_start, timestamp, reservation_id=...) -> None: ...

@dataclass
class StopTransaction:
    meter_stop: int
    timestamp: str
    transaction_id: int
    reason: Reason | None = ...
    id_tag: str | None = ...
    transaction_data: list | None = ...
    def __init__(self, meter_stop, timestamp, transaction_id, reason=..., id_tag=..., transaction_data=...) -> None: ...

@dataclass
class StatusNotification:
    connector_id: int
    error_code: ChargePointErrorCode
    status: ChargePointStatus
    timestamp: str | None = ...
    info: str | None = ...
    vendor_id: str | None = ...
    vendor_error_code: str | None = ...
    def __init__(self, connector_id, error_code, status, timestamp=..., info=..., vendor_id=..., vendor_error_code=...) -> None: ...

@dataclass
class DataTransfer:
    vendor_id: str
    message_id: str | None = ...
    data: str | None = ...
    def __init__(self, vendor_id, message_id=..., data=...) -> None: ...

@dataclass
class CancelReservationPayload(CancelReservation):
    def __post_init__(self) -> None: ...
    def __init__(self, reservation_id) -> None: ...

@dataclass
class CertificateSignedPayload(CertificateSigned):
    def __post_init__(self) -> None: ...
    def __init__(self, certificate_chain) -> None: ...

@dataclass
class ChangeAvailabilityPayload(ChangeAvailability):
    def __post_init__(self) -> None: ...
    def __init__(self, connector_id, type) -> None: ...

@dataclass
class ChangeConfigurationPayload(ChangeConfiguration):
    def __post_init__(self) -> None: ...
    def __init__(self, key, value) -> None: ...

@dataclass
class ClearCachePayload(ClearCache):
    def __post_init__(self) -> None: ...

@dataclass
class ClearChargingProfilePayload(ClearChargingProfile):
    def __post_init__(self) -> None: ...
    def __init__(self, id=..., connector_id=..., charging_profile_purpose=..., stack_level=...) -> None: ...

@dataclass
class DeleteCertificatePayload(DeleteCertificate):
    def __post_init__(self) -> None: ...
    def __init__(self, certificate_hash_data) -> None: ...

@dataclass
class ExtendedTriggerMessagePayload(ExtendedTriggerMessage):
    def __post_init__(self) -> None: ...
    def __init__(self, requested_message, connector_id=...) -> None: ...

@dataclass
class GetCompositeSchedulePayload(GetCompositeSchedule):
    def __post_init__(self) -> None: ...
    def __init__(self, connector_id, duration, charging_rate_unit=...) -> None: ...

@dataclass
class GetConfigurationPayload(GetConfiguration):
    def __post_init__(self) -> None: ...
    def __init__(self, key=...) -> None: ...

@dataclass
class GetDiagnosticsPayload(GetDiagnostics):
    def __post_init__(self) -> None: ...
    def __init__(self, location, retries=..., retry_interval=..., start_time=..., stop_time=...) -> None: ...

@dataclass
class GetInstalledCertificateIdsPayload(GetInstalledCertificateIds):
    def __post_init__(self) -> None: ...
    def __init__(self, certificate_type) -> None: ...

@dataclass
class GetLocalListVersionPayload(GetLocalListVersion):
    def __post_init__(self) -> None: ...

@dataclass
class GetLogPayload(GetLog):
    def __post_init__(self) -> None: ...
    def __init__(self, log, log_type, request_id, retries=..., retry_interval=...) -> None: ...

@dataclass
class InstallCertificatePayload(InstallCertificate):
    def __post_init__(self) -> None: ...
    def __init__(self, certificate_type, certificate) -> None: ...

@dataclass
class RemoteStartTransactionPayload(RemoteStartTransaction):
    def __post_init__(self) -> None: ...
    def __init__(self, id_tag, connector_id=..., charging_profile=...) -> None: ...

@dataclass
class RemoteStopTransactionPayload(RemoteStopTransaction):
    def __post_init__(self) -> None: ...
    def __init__(self, transaction_id) -> None: ...

@dataclass
class ReserveNowPayload(ReserveNow):
    def __post_init__(self) -> None: ...
    def __init__(self, connector_id, expiry_date, id_tag, reservation_id, parent_id_tag=...) -> None: ...

@dataclass
class ResetPayload(Reset):
    def __post_init__(self) -> None: ...
    def __init__(self, type) -> None: ...

@dataclass
class SendLocalListPayload(SendLocalList):
    def __post_init__(self) -> None: ...
    def __init__(self, list_version, update_type, local_authorization_list=...) -> None: ...

@dataclass
class SetChargingProfilePayload(SetChargingProfile):
    def __post_init__(self) -> None: ...
    def __init__(self, connector_id, cs_charging_profiles) -> None: ...

@dataclass
class SignedUpdateFirmwarePayload(SignedUpdateFirmware):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, firmware, retries=..., retry_interval=...) -> None: ...

@dataclass
class TriggerMessagePayload(TriggerMessage):
    def __post_init__(self) -> None: ...
    def __init__(self, requested_message, connector_id=...) -> None: ...

@dataclass
class UnlockConnectorPayload(UnlockConnector):
    def __post_init__(self) -> None: ...
    def __init__(self, connector_id) -> None: ...

@dataclass
class UpdateFirmwarePayload(UpdateFirmware):
    def __post_init__(self) -> None: ...
    def __init__(self, location, retrieve_date, retries=..., retry_interval=...) -> None: ...

@dataclass
class AuthorizePayload(Authorize):
    def __post_init__(self) -> None: ...
    def __init__(self, id_tag) -> None: ...

@dataclass
class BootNotificationPayload(BootNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, charge_point_model, charge_point_vendor, charge_box_serial_number=..., charge_point_serial_number=..., firmware_version=..., iccid=..., imsi=..., meter_serial_number=..., meter_type=...) -> None: ...

@dataclass
class DiagnosticsStatusNotificationPayload(DiagnosticsStatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, status) -> None: ...

@dataclass
class FirmwareStatusNotificationPayload(FirmwareStatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, status) -> None: ...

@dataclass
class HeartbeatPayload(Heartbeat):
    def __post_init__(self) -> None: ...

@dataclass
class LogStatusNotificationPayload(LogStatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, status, request_id) -> None: ...

@dataclass
class MeterValuesPayload(MeterValues):
    def __post_init__(self) -> None: ...
    def __init__(self, connector_id, meter_value=..., transaction_id=...) -> None: ...

@dataclass
class SecurityEventNotificationPayload(SecurityEventNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, type, timestamp, tech_info) -> None: ...

@dataclass
class SignCertificatePayload(SignCertificate):
    def __post_init__(self) -> None: ...
    def __init__(self, csr) -> None: ...

@dataclass
class SignedFirmwareStatusNotificationPayload(SignedFirmwareStatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, status, request_id) -> None: ...

@dataclass
class StartTransactionPayload(StartTransaction):
    def __post_init__(self) -> None: ...
    def __init__(self, connector_id, id_tag, meter_start, timestamp, reservation_id=...) -> None: ...

@dataclass
class StopTransactionPayload(StopTransaction):
    def __post_init__(self) -> None: ...
    def __init__(self, meter_stop, timestamp, transaction_id, reason=..., id_tag=..., transaction_data=...) -> None: ...

@dataclass
class StatusNotificationPayload(StatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, connector_id, error_code, status, timestamp=..., info=..., vendor_id=..., vendor_error_code=...) -> None: ...

@dataclass
class DataTransferPayload(DataTransfer):
    def __post_init__(self) -> None: ...
    def __init__(self, vendor_id, message_id=..., data=...) -> None: ...