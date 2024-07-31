from dataclasses import dataclass
from typing import Any

@dataclass
class Authorize:
    id_token: dict
    certificate: str | None = ...
    iso15118_certificate_hash_data: list | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, id_token, certificate=..., iso15118_certificate_hash_data=..., custom_data=...) -> None: ...

@dataclass
class BootNotification:
    charging_station: dict
    reason: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, charging_station, reason, custom_data=...) -> None: ...

@dataclass
class CancelReservation:
    reservation_id: int
    custom_data: dict[str, Any] | None = ...
    def __init__(self, reservation_id, custom_data=...) -> None: ...

@dataclass
class CertificateSigned:
    certificate_chain: str
    certificate_type: str | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, certificate_chain, certificate_type=..., custom_data=...) -> None: ...

@dataclass
class ChangeAvailability:
    operational_status: str
    evse: dict | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, operational_status, evse=..., custom_data=...) -> None: ...

@dataclass
class ClearCache:
    custom_data: dict[str, Any] | None = ...
    def __init__(self, custom_data=...) -> None: ...

@dataclass
class ClearChargingProfile:
    charging_profile_id: int | None = ...
    charging_profile_criteria: dict | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, charging_profile_id=..., charging_profile_criteria=..., custom_data=...) -> None: ...

@dataclass
class ClearDisplayMessage:
    id: int
    custom_data: dict[str, Any] | None = ...
    def __init__(self, id, custom_data=...) -> None: ...

@dataclass
class ClearVariableMonitoring:
    id: list
    custom_data: dict[str, Any] | None = ...
    def __init__(self, id, custom_data=...) -> None: ...

@dataclass
class ClearedChargingLimit:
    charging_limit_source: str
    evse_id: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, charging_limit_source, evse_id=..., custom_data=...) -> None: ...

@dataclass
class CostUpdated:
    total_cost: float
    transaction_id: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, total_cost, transaction_id, custom_data=...) -> None: ...

@dataclass
class CustomerInformation:
    request_id: int
    report: bool
    clear: bool
    customer_certificate: dict | None = ...
    id_token: dict | None = ...
    customer_identifier: str | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, report, clear, customer_certificate=..., id_token=..., customer_identifier=..., custom_data=...) -> None: ...

@dataclass
class DataTransfer:
    vendor_id: str
    message_id: str | None = ...
    data: Any | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, vendor_id, message_id=..., data=..., custom_data=...) -> None: ...

@dataclass
class DeleteCertificate:
    certificate_hash_data: dict
    custom_data: dict[str, Any] | None = ...
    def __init__(self, certificate_hash_data, custom_data=...) -> None: ...

@dataclass
class FirmwareStatusNotification:
    status: str
    request_id: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, status, request_id=..., custom_data=...) -> None: ...

@dataclass
class Get15118EVCertificate:
    iso15118_schema_version: str
    action: str
    exi_request: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, iso15118_schema_version, action, exi_request, custom_data=...) -> None: ...

@dataclass
class GetBaseReport:
    request_id: int
    report_base: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, report_base, custom_data=...) -> None: ...

@dataclass
class GetCertificateStatus:
    ocsp_request_data: dict
    custom_data: dict[str, Any] | None = ...
    def __init__(self, ocsp_request_data, custom_data=...) -> None: ...

@dataclass
class GetChargingProfiles:
    request_id: int
    charging_profile: dict
    evse_id: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, charging_profile, evse_id=..., custom_data=...) -> None: ...

@dataclass
class GetCompositeSchedule:
    duration: int
    evse_id: int
    charging_rate_unit: str | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, duration, evse_id, charging_rate_unit=..., custom_data=...) -> None: ...

@dataclass
class GetDisplayMessages:
    request_id: int
    id: list | None = ...
    priority: str | None = ...
    state: str | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, id=..., priority=..., state=..., custom_data=...) -> None: ...

@dataclass
class GetInstalledCertificateIds:
    certificate_type: list | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, certificate_type=..., custom_data=...) -> None: ...

@dataclass
class GetLocalListVersion:
    custom_data: dict[str, Any] | None = ...
    def __init__(self, custom_data=...) -> None: ...

@dataclass
class GetLog:
    log: dict
    log_type: str
    request_id: int
    retries: int | None = ...
    retry_interval: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, log, log_type, request_id, retries=..., retry_interval=..., custom_data=...) -> None: ...

@dataclass
class GetMonitoringReport:
    request_id: int
    component_variable: list | None = ...
    monitoring_criteria: list | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, component_variable=..., monitoring_criteria=..., custom_data=...) -> None: ...

@dataclass
class GetReport:
    request_id: int
    component_variable: list | None = ...
    component_criteria: list | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, component_variable=..., component_criteria=..., custom_data=...) -> None: ...

@dataclass
class GetTransactionStatus:
    transaction_id: str | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, transaction_id=..., custom_data=...) -> None: ...

@dataclass
class GetVariables:
    get_variable_data: list
    custom_data: dict[str, Any] | None = ...
    def __init__(self, get_variable_data, custom_data=...) -> None: ...

@dataclass
class Heartbeat:
    custom_data: dict[str, Any] | None = ...
    def __init__(self, custom_data=...) -> None: ...

@dataclass
class InstallCertificate:
    certificate_type: str
    certificate: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, certificate_type, certificate, custom_data=...) -> None: ...

@dataclass
class LogStatusNotification:
    status: str
    request_id: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, status, request_id=..., custom_data=...) -> None: ...

@dataclass
class MeterValues:
    evse_id: int
    meter_value: list
    custom_data: dict[str, Any] | None = ...
    def __init__(self, evse_id, meter_value, custom_data=...) -> None: ...

@dataclass
class NotifyChargingLimit:
    charging_limit: dict
    charging_schedule: list | None = ...
    evse_id: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, charging_limit, charging_schedule=..., evse_id=..., custom_data=...) -> None: ...

@dataclass
class NotifyCustomerInformation:
    data: str
    seq_no: int
    generated_at: str
    request_id: int
    tbc: bool | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, data, seq_no, generated_at, request_id, tbc=..., custom_data=...) -> None: ...

@dataclass
class NotifyDisplayMessages:
    request_id: int
    message_info: list | None = ...
    tbc: bool | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, message_info=..., tbc=..., custom_data=...) -> None: ...

@dataclass
class NotifyEVChargingNeeds:
    charging_needs: dict
    evse_id: int
    max_schedule_tuples: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, charging_needs, evse_id, max_schedule_tuples=..., custom_data=...) -> None: ...

@dataclass
class NotifyEVChargingSchedule:
    time_base: str
    charging_schedule: dict
    evse_id: int
    custom_data: dict[str, Any] | None = ...
    def __init__(self, time_base, charging_schedule, evse_id, custom_data=...) -> None: ...

@dataclass
class NotifyEvent:
    generated_at: str
    seq_no: int
    event_data: list
    tbc: bool | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, generated_at, seq_no, event_data, tbc=..., custom_data=...) -> None: ...

@dataclass
class NotifyMonitoringReport:
    request_id: int
    seq_no: int
    generated_at: str
    monitor: list | None = ...
    tbc: bool | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, seq_no, generated_at, monitor=..., tbc=..., custom_data=...) -> None: ...

@dataclass
class NotifyReport:
    request_id: int
    generated_at: str
    seq_no: int
    report_data: list | None = ...
    tbc: bool | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, generated_at, seq_no, report_data=..., tbc=..., custom_data=...) -> None: ...

@dataclass
class PublishFirmware:
    location: str
    checksum: str
    request_id: int
    retries: int | None = ...
    retry_interval: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, location, checksum, request_id, retries=..., retry_interval=..., custom_data=...) -> None: ...

@dataclass
class PublishFirmwareStatusNotification:
    status: str
    location: list | None = ...
    request_id: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, status, location=..., request_id=..., custom_data=...) -> None: ...

@dataclass
class ReportChargingProfiles:
    request_id: int
    charging_limit_source: str
    charging_profile: list
    evse_id: int
    tbc: bool | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, charging_limit_source, charging_profile, evse_id, tbc=..., custom_data=...) -> None: ...

@dataclass
class RequestStartTransaction:
    id_token: dict
    remote_start_id: int
    evse_id: int | None = ...
    group_id_token: dict | None = ...
    charging_profile: dict | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, id_token, remote_start_id, evse_id=..., group_id_token=..., charging_profile=..., custom_data=...) -> None: ...

@dataclass
class RequestStopTransaction:
    transaction_id: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, transaction_id, custom_data=...) -> None: ...

@dataclass
class ReservationStatusUpdate:
    reservation_id: int
    reservation_update_status: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, reservation_id, reservation_update_status, custom_data=...) -> None: ...

@dataclass
class ReserveNow:
    id: int
    expiry_date_time: str
    id_token: dict
    connector_type: str | None = ...
    evse_id: int | None = ...
    group_id_token: dict | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, id, expiry_date_time, id_token, connector_type=..., evse_id=..., group_id_token=..., custom_data=...) -> None: ...

@dataclass
class Reset:
    type: str
    evse_id: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, type, evse_id=..., custom_data=...) -> None: ...

@dataclass
class SecurityEventNotification:
    type: str
    timestamp: str
    tech_info: str | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, type, timestamp, tech_info=..., custom_data=...) -> None: ...

@dataclass
class SendLocalList:
    version_number: int
    update_type: str
    local_authorization_list: list | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, version_number, update_type, local_authorization_list=..., custom_data=...) -> None: ...

@dataclass
class SetChargingProfile:
    evse_id: int
    charging_profile: dict
    custom_data: dict[str, Any] | None = ...
    def __init__(self, evse_id, charging_profile, custom_data=...) -> None: ...

@dataclass
class SetDisplayMessage:
    message: dict
    custom_data: dict[str, Any] | None = ...
    def __init__(self, message, custom_data=...) -> None: ...

@dataclass
class SetMonitoringBase:
    monitoring_base: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, monitoring_base, custom_data=...) -> None: ...

@dataclass
class SetMonitoringLevel:
    severity: int
    custom_data: dict[str, Any] | None = ...
    def __init__(self, severity, custom_data=...) -> None: ...

@dataclass
class SetNetworkProfile:
    configuration_slot: int
    connection_data: dict
    custom_data: dict[str, Any] | None = ...
    def __init__(self, configuration_slot, connection_data, custom_data=...) -> None: ...

@dataclass
class SetVariableMonitoring:
    set_monitoring_data: list
    custom_data: dict[str, Any] | None = ...
    def __init__(self, set_monitoring_data, custom_data=...) -> None: ...

@dataclass
class SetVariables:
    set_variable_data: list
    custom_data: dict[str, Any] | None = ...
    def __init__(self, set_variable_data, custom_data=...) -> None: ...

@dataclass
class SignCertificate:
    csr: str
    certificate_type: str | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, csr, certificate_type=..., custom_data=...) -> None: ...

@dataclass
class StatusNotification:
    timestamp: str
    connector_status: str
    evse_id: int
    connector_id: int
    custom_data: dict[str, Any] | None = ...
    def __init__(self, timestamp, connector_status, evse_id, connector_id, custom_data=...) -> None: ...

@dataclass
class TransactionEvent:
    event_type: str
    timestamp: str
    trigger_reason: str
    seq_no: int
    transaction_info: dict
    meter_value: list | None = ...
    offline: bool | None = ...
    number_of_phases_used: int | None = ...
    cable_max_current: int | None = ...
    reservation_id: int | None = ...
    evse: dict | None = ...
    id_token: dict | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, event_type, timestamp, trigger_reason, seq_no, transaction_info, meter_value=..., offline=..., number_of_phases_used=..., cable_max_current=..., reservation_id=..., evse=..., id_token=..., custom_data=...) -> None: ...

@dataclass
class TriggerMessage:
    requested_message: str
    evse: dict | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, requested_message, evse=..., custom_data=...) -> None: ...

@dataclass
class UnlockConnector:
    evse_id: int
    connector_id: int
    custom_data: dict[str, Any] | None = ...
    def __init__(self, evse_id, connector_id, custom_data=...) -> None: ...

@dataclass
class UnpublishFirmware:
    checksum: str
    custom_data: dict[str, Any] | None = ...
    def __init__(self, checksum, custom_data=...) -> None: ...

@dataclass
class UpdateFirmware:
    request_id: int
    firmware: dict
    retries: int | None = ...
    retry_interval: int | None = ...
    custom_data: dict[str, Any] | None = ...
    def __init__(self, request_id, firmware, retries=..., retry_interval=..., custom_data=...) -> None: ...

@dataclass
class AuthorizePayload(Authorize):
    def __post_init__(self) -> None: ...
    def __init__(self, id_token, certificate=..., iso15118_certificate_hash_data=..., custom_data=...) -> None: ...

@dataclass
class BootNotificationPayload(BootNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, charging_station, reason, custom_data=...) -> None: ...

@dataclass
class CancelReservationPayload(CancelReservation):
    def __post_init__(self) -> None: ...
    def __init__(self, reservation_id, custom_data=...) -> None: ...

@dataclass
class CertificateSignedPayload(CertificateSigned):
    def __post_init__(self) -> None: ...
    def __init__(self, certificate_chain, certificate_type=..., custom_data=...) -> None: ...

@dataclass
class ChangeAvailabilityPayload(ChangeAvailability):
    def __post_init__(self) -> None: ...
    def __init__(self, operational_status, evse=..., custom_data=...) -> None: ...

@dataclass
class ClearCachePayload(ClearCache):
    def __post_init__(self) -> None: ...
    def __init__(self, custom_data=...) -> None: ...

@dataclass
class ClearChargingProfilePayload(ClearChargingProfile):
    def __post_init__(self) -> None: ...
    def __init__(self, charging_profile_id=..., charging_profile_criteria=..., custom_data=...) -> None: ...

@dataclass
class ClearDisplayMessagePayload(ClearDisplayMessage):
    def __post_init__(self) -> None: ...
    def __init__(self, id, custom_data=...) -> None: ...

@dataclass
class ClearVariableMonitoringPayload(ClearVariableMonitoring):
    def __post_init__(self) -> None: ...
    def __init__(self, id, custom_data=...) -> None: ...

@dataclass
class ClearedChargingLimitPayload(ClearedChargingLimit):
    def __post_init__(self) -> None: ...
    def __init__(self, charging_limit_source, evse_id=..., custom_data=...) -> None: ...

@dataclass
class CostUpdatedPayload(CostUpdated):
    def __post_init__(self) -> None: ...
    def __init__(self, total_cost, transaction_id, custom_data=...) -> None: ...

@dataclass
class CustomerInformationPayload(CustomerInformation):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, report, clear, customer_certificate=..., id_token=..., customer_identifier=..., custom_data=...) -> None: ...

@dataclass
class DataTransferPayload(DataTransfer):
    def __post_init__(self) -> None: ...
    def __init__(self, vendor_id, message_id=..., data=..., custom_data=...) -> None: ...

@dataclass
class DeleteCertificatePayload(DeleteCertificate):
    def __post_init__(self) -> None: ...
    def __init__(self, certificate_hash_data, custom_data=...) -> None: ...

@dataclass
class FirmwareStatusNotificationPayload(FirmwareStatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, status, request_id=..., custom_data=...) -> None: ...

@dataclass
class Get15118EVCertificatePayload(Get15118EVCertificate):
    def __post_init__(self) -> None: ...
    def __init__(self, iso15118_schema_version, action, exi_request, custom_data=...) -> None: ...

@dataclass
class GetBaseReportPayload(GetBaseReport):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, report_base, custom_data=...) -> None: ...

@dataclass
class GetCertificateStatusPayload(GetCertificateStatus):
    def __post_init__(self) -> None: ...
    def __init__(self, ocsp_request_data, custom_data=...) -> None: ...

@dataclass
class GetChargingProfilesPayload(GetChargingProfiles):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, charging_profile, evse_id=..., custom_data=...) -> None: ...

@dataclass
class GetCompositeSchedulePayload(GetCompositeSchedule):
    def __post_init__(self) -> None: ...
    def __init__(self, duration, evse_id, charging_rate_unit=..., custom_data=...) -> None: ...

@dataclass
class GetDisplayMessagesPayload(GetDisplayMessages):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, id=..., priority=..., state=..., custom_data=...) -> None: ...

@dataclass
class GetInstalledCertificateIdsPayload(GetInstalledCertificateIds):
    def __post_init__(self) -> None: ...
    def __init__(self, certificate_type=..., custom_data=...) -> None: ...

@dataclass
class GetLocalListVersionPayload(GetLocalListVersion):
    def __post_init__(self) -> None: ...
    def __init__(self, custom_data=...) -> None: ...

@dataclass
class GetLogPayload(GetLog):
    def __post_init__(self) -> None: ...
    def __init__(self, log, log_type, request_id, retries=..., retry_interval=..., custom_data=...) -> None: ...

@dataclass
class GetMonitoringReportPayload(GetMonitoringReport):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, component_variable=..., monitoring_criteria=..., custom_data=...) -> None: ...

@dataclass
class GetReportPayload(GetReport):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, component_variable=..., component_criteria=..., custom_data=...) -> None: ...

@dataclass
class GetTransactionStatusPayload(GetTransactionStatus):
    def __post_init__(self) -> None: ...
    def __init__(self, transaction_id=..., custom_data=...) -> None: ...

@dataclass
class GetVariablesPayload(GetVariables):
    def __post_init__(self) -> None: ...
    def __init__(self, get_variable_data, custom_data=...) -> None: ...

@dataclass
class HeartbeatPayload(Heartbeat):
    def __post_init__(self) -> None: ...
    def __init__(self, custom_data=...) -> None: ...

@dataclass
class InstallCertificatePayload(InstallCertificate):
    def __post_init__(self) -> None: ...
    def __init__(self, certificate_type, certificate, custom_data=...) -> None: ...

@dataclass
class LogStatusNotificationPayload(LogStatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, status, request_id=..., custom_data=...) -> None: ...

@dataclass
class MeterValuesPayload(MeterValues):
    def __post_init__(self) -> None: ...
    def __init__(self, evse_id, meter_value, custom_data=...) -> None: ...

@dataclass
class NotifyChargingLimitPayload(NotifyChargingLimit):
    def __post_init__(self) -> None: ...
    def __init__(self, charging_limit, charging_schedule=..., evse_id=..., custom_data=...) -> None: ...

@dataclass
class NotifyCustomerInformationPayload(NotifyCustomerInformation):
    def __post_init__(self) -> None: ...
    def __init__(self, data, seq_no, generated_at, request_id, tbc=..., custom_data=...) -> None: ...

@dataclass
class NotifyDisplayMessagesPayload(NotifyDisplayMessages):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, message_info=..., tbc=..., custom_data=...) -> None: ...

@dataclass
class NotifyEVChargingNeedsPayload(NotifyEVChargingNeeds):
    def __post_init__(self) -> None: ...
    def __init__(self, charging_needs, evse_id, max_schedule_tuples=..., custom_data=...) -> None: ...

@dataclass
class NotifyEVChargingSchedulePayload(NotifyEVChargingSchedule):
    def __post_init__(self) -> None: ...
    def __init__(self, time_base, charging_schedule, evse_id, custom_data=...) -> None: ...

@dataclass
class NotifyEventPayload(NotifyEvent):
    def __post_init__(self) -> None: ...
    def __init__(self, generated_at, seq_no, event_data, tbc=..., custom_data=...) -> None: ...

@dataclass
class NotifyMonitoringReportPayload(NotifyMonitoringReport):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, seq_no, generated_at, monitor=..., tbc=..., custom_data=...) -> None: ...

@dataclass
class NotifyReportPayload(NotifyReport):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, generated_at, seq_no, report_data=..., tbc=..., custom_data=...) -> None: ...

@dataclass
class PublishFirmwarePayload(PublishFirmware):
    def __post_init__(self) -> None: ...
    def __init__(self, location, checksum, request_id, retries=..., retry_interval=..., custom_data=...) -> None: ...

@dataclass
class PublishFirmwareStatusNotificationPayload(PublishFirmwareStatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, status, location=..., request_id=..., custom_data=...) -> None: ...

@dataclass
class ReportChargingProfilesPayload(ReportChargingProfiles):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, charging_limit_source, charging_profile, evse_id, tbc=..., custom_data=...) -> None: ...

@dataclass
class RequestStartTransactionPayload(RequestStartTransaction):
    def __post_init__(self) -> None: ...
    def __init__(self, id_token, remote_start_id, evse_id=..., group_id_token=..., charging_profile=..., custom_data=...) -> None: ...

@dataclass
class RequestStopTransactionPayload(RequestStopTransaction):
    def __post_init__(self) -> None: ...
    def __init__(self, transaction_id, custom_data=...) -> None: ...

@dataclass
class ReservationStatusUpdatePayload(ReservationStatusUpdate):
    def __post_init__(self) -> None: ...
    def __init__(self, reservation_id, reservation_update_status, custom_data=...) -> None: ...

@dataclass
class ReserveNowPayload(ReserveNow):
    def __post_init__(self) -> None: ...
    def __init__(self, id, expiry_date_time, id_token, connector_type=..., evse_id=..., group_id_token=..., custom_data=...) -> None: ...

@dataclass
class ResetPayload(Reset):
    def __post_init__(self) -> None: ...
    def __init__(self, type, evse_id=..., custom_data=...) -> None: ...

@dataclass
class SecurityEventNotificationPayload(SecurityEventNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, type, timestamp, tech_info=..., custom_data=...) -> None: ...

@dataclass
class SendLocalListPayload(SendLocalList):
    def __post_init__(self) -> None: ...
    def __init__(self, version_number, update_type, local_authorization_list=..., custom_data=...) -> None: ...

@dataclass
class SetChargingProfilePayload(SetChargingProfile):
    def __post_init__(self) -> None: ...
    def __init__(self, evse_id, charging_profile, custom_data=...) -> None: ...

@dataclass
class SetDisplayMessagePayload(SetDisplayMessage):
    def __post_init__(self) -> None: ...
    def __init__(self, message, custom_data=...) -> None: ...

@dataclass
class SetMonitoringBasePayload(SetMonitoringBase):
    def __post_init__(self) -> None: ...
    def __init__(self, monitoring_base, custom_data=...) -> None: ...

@dataclass
class SetMonitoringLevelPayload(SetMonitoringLevel):
    def __post_init__(self) -> None: ...
    def __init__(self, severity, custom_data=...) -> None: ...

@dataclass
class SetNetworkProfilePayload(SetNetworkProfile):
    def __post_init__(self) -> None: ...
    def __init__(self, configuration_slot, connection_data, custom_data=...) -> None: ...

@dataclass
class SetVariableMonitoringPayload(SetVariableMonitoring):
    def __post_init__(self) -> None: ...
    def __init__(self, set_monitoring_data, custom_data=...) -> None: ...

@dataclass
class SetVariablesPayload(SetVariables):
    def __post_init__(self) -> None: ...
    def __init__(self, set_variable_data, custom_data=...) -> None: ...

@dataclass
class SignCertificatePayload(SignCertificate):
    def __post_init__(self) -> None: ...
    def __init__(self, csr, certificate_type=..., custom_data=...) -> None: ...

@dataclass
class StatusNotificationPayload(StatusNotification):
    def __post_init__(self) -> None: ...
    def __init__(self, timestamp, connector_status, evse_id, connector_id, custom_data=...) -> None: ...

@dataclass
class TransactionEventPayload(TransactionEvent):
    def __post_init__(self) -> None: ...
    def __init__(self, event_type, timestamp, trigger_reason, seq_no, transaction_info, meter_value=..., offline=..., number_of_phases_used=..., cable_max_current=..., reservation_id=..., evse=..., id_token=..., custom_data=...) -> None: ...

@dataclass
class TriggerMessagePayload(TriggerMessage):
    def __post_init__(self) -> None: ...
    def __init__(self, requested_message, evse=..., custom_data=...) -> None: ...

@dataclass
class UnlockConnectorPayload(UnlockConnector):
    def __post_init__(self) -> None: ...
    def __init__(self, evse_id, connector_id, custom_data=...) -> None: ...

@dataclass
class UnpublishFirmwarePayload(UnpublishFirmware):
    def __post_init__(self) -> None: ...
    def __init__(self, checksum, custom_data=...) -> None: ...

@dataclass
class UpdateFirmwarePayload(UpdateFirmware):
    def __post_init__(self) -> None: ...
    def __init__(self, request_id, firmware, retries=..., retry_interval=..., custom_data=...) -> None: ...