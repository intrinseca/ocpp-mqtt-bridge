from dataclasses import dataclass

from ocpp.v201 import enums as enums

@dataclass
class ACChargingParametersType:
    energy_amount: int
    ev_min_current: int
    ev_max_current: int
    ev_max_voltage: int
    def __init__(
        self, energy_amount, ev_min_current, ev_max_current, ev_max_voltage
    ) -> None: ...

@dataclass
class AdditionalInfoType:
    additional_id_token: str
    type: str
    def __init__(self, additional_id_token, type) -> None: ...

@dataclass
class APNType:
    apn: str
    apn_authentication: enums.APNAuthenticationType
    apn_user_name: str | None = ...
    apn_password: str | None = ...
    sim_pin: int | None = ...
    preferred_network: str | None = ...
    use_only_preferred_network: bool | None = ...
    def __init__(
        self,
        apn,
        apn_authentication,
        apn_user_name=...,
        apn_password=...,
        sim_pin=...,
        preferred_network=...,
        use_only_preferred_network=...,
    ) -> None: ...

@dataclass
class CertificateHashDataType:
    hash_algorithm: enums.HashAlgorithmType
    issuer_name_hash: str
    issuer_key_hash: str
    serial_number: str
    def __init__(
        self, hash_algorithm, issuer_name_hash, issuer_key_hash, serial_number
    ) -> None: ...

@dataclass
class CertificateHashDataChainType:
    certificate_type: enums.GetCertificateIdUseType
    certificate_hash_data: CertificateHashDataType
    child_certificate_hash_data: list[CertificateHashDataType] | None = ...
    def __init__(
        self, certificate_type, certificate_hash_data, child_certificate_hash_data=...
    ) -> None: ...

@dataclass
class ChargingLimitType:
    charging_limit_source: enums.ChargingLimitSourceType
    is_grid_critical: bool | None = ...
    def __init__(self, charging_limit_source, is_grid_critical=...) -> None: ...

@dataclass
class DCChargingParametersType:
    ev_max_current: int
    ev_max_voltage: int
    energy_amount: int | None = ...
    ev_max_power: int | None = ...
    state_of_charge: int | None = ...
    ev_energy_capacity: int | None = ...
    full_soc: int | None = ...
    bulk_soc: int | None = ...
    def __init__(
        self,
        ev_max_current,
        ev_max_voltage,
        energy_amount=...,
        ev_max_power=...,
        state_of_charge=...,
        ev_energy_capacity=...,
        full_soc=...,
        bulk_soc=...,
    ) -> None: ...

@dataclass
class ChargingNeedsType:
    requested_energy_transfer: enums.EnergyTransferModeType
    departure_time: str | None = ...
    ac_charging_parameters: ACChargingParametersType | None = ...
    dc_charging_parameters: DCChargingParametersType | None = ...
    def __init__(
        self,
        requested_energy_transfer,
        departure_time=...,
        ac_charging_parameters=...,
        dc_charging_parameters=...,
    ) -> None: ...

@dataclass
class ChargingProfileCriterionType:
    charging_profile_purpose: enums.ChargingProfilePurposeType | None = ...
    stack_level: int | None = ...
    charging_profile_id: list[int] | None = ...
    charging_limit_source: list[enums.ChargingLimitSourceType] | None = ...
    def __init__(
        self,
        charging_profile_purpose=...,
        stack_level=...,
        charging_profile_id=...,
        charging_limit_source=...,
    ) -> None: ...

@dataclass
class ChargingSchedulePeriodType:
    start_period: int
    limit: float
    number_phases: int | None = ...
    phase_to_use: int | None = ...
    def __init__(
        self, start_period, limit, number_phases=..., phase_to_use=...
    ) -> None: ...

@dataclass
class RelativeTimeIntervalType:
    start: int
    duration: int | None = ...
    def __init__(self, start, duration=...) -> None: ...

@dataclass
class CostType:
    cost_kind: enums.CostKindType
    amount: int
    amount_multiplier: int | None = ...
    def __init__(self, cost_kind, amount, amount_multiplier=...) -> None: ...

@dataclass
class ConsumptionCostType:
    start_value: float
    cost: list[CostType]
    def __init__(self, start_value, cost) -> None: ...

@dataclass
class SalesTariffEntryType:
    relative_time_interval: RelativeTimeIntervalType
    consumption_cost: list[ConsumptionCostType] | None = ...
    e_price_level: int | None = ...
    def __init__(
        self, relative_time_interval, consumption_cost=..., e_price_level=...
    ) -> None: ...

@dataclass
class SalesTariffType:
    id: int
    sales_tariff_entry: list[SalesTariffEntryType]
    sales_tariff_description: str | None = ...
    num_e_price_levels: int | None = ...
    def __init__(
        self,
        id,
        sales_tariff_entry,
        sales_tariff_description=...,
        num_e_price_levels=...,
    ) -> None: ...

@dataclass
class ChargingScheduleType:
    id: int
    charging_rate_unit: enums.ChargingRateUnitType
    charging_schedule_period: list[ChargingSchedulePeriodType]
    start_schedule: str | None = ...
    duration: int | None = ...
    min_charging_rate: float | None = ...
    sales_tariff: SalesTariffType | None = ...
    def __init__(
        self,
        id,
        charging_rate_unit,
        charging_schedule_period,
        start_schedule=...,
        duration=...,
        min_charging_rate=...,
        sales_tariff=...,
    ) -> None: ...

@dataclass
class ChargingProfileType:
    id: int
    stack_level: int
    charging_profile_purpose: enums.ChargingProfilePurposeType
    charging_profile_kind: enums.ChargingProfileKindType
    charging_schedule: list[ChargingScheduleType]
    valid_from: str | None = ...
    valid_to: str | None = ...
    transaction_id: str | None = ...
    recurrency_kind: enums.RecurrencyKindType | None = ...
    def __init__(
        self,
        id,
        stack_level,
        charging_profile_purpose,
        charging_profile_kind,
        charging_schedule,
        valid_from=...,
        valid_to=...,
        transaction_id=...,
        recurrency_kind=...,
    ) -> None: ...

@dataclass
class ClearChargingProfileType:
    evse_id: int | None = ...
    charging_profile_purpose: enums.ChargingProfilePurposeType | None = ...
    stack_level: int | None = ...
    def __init__(
        self, evse_id=..., charging_profile_purpose=..., stack_level=...
    ) -> None: ...

@dataclass
class StatusInfoType:
    reason_code: str
    additional_info: str | None = ...
    def __init__(self, reason_code, additional_info=...) -> None: ...

@dataclass
class ClearMonitoringResultType:
    status: enums.ClearMonitoringStatusType
    id: int
    status_info: StatusInfoType | None = ...
    def __init__(self, status, id, status_info=...) -> None: ...

@dataclass
class EVSEType:
    id: int
    connector_id: int | None = ...
    def __init__(self, id, connector_id=...) -> None: ...

@dataclass
class ComponentType:
    name: str
    instance: str | None = ...
    evse: EVSEType | None = ...
    def __init__(self, name, instance=..., evse=...) -> None: ...

@dataclass
class VariableType:
    name: str
    instance: str | None = ...
    def __init__(self, name, instance=...) -> None: ...

@dataclass
class ComponentVariableType:
    component: ComponentType
    variable: VariableType | None = ...
    def __init__(self, component, variable=...) -> None: ...

@dataclass
class CompositeScheduleType:
    evse_id: int
    duration: int
    schedule_start: str
    charging_rate_unit: enums.ChargingRateUnitType
    charging_schedule_period: list[ChargingSchedulePeriodType]
    def __init__(
        self,
        evse_id,
        duration,
        schedule_start,
        charging_rate_unit,
        charging_schedule_period,
    ) -> None: ...

@dataclass
class EventDataType:
    event_id: int
    timestamp: str
    trigger: enums.EventTriggerType
    actual_value: str
    event_notification_type: enums.EventNotificationType
    component: ComponentType
    variable: VariableType
    cause: int | None = ...
    tech_code: str | None = ...
    tech_info: str | None = ...
    cleared: bool | None = ...
    transaction_id: str | None = ...
    variable_monitoring_id: int | None = ...
    def __init__(
        self,
        event_id,
        timestamp,
        trigger,
        actual_value,
        event_notification_type,
        component,
        variable,
        cause=...,
        tech_code=...,
        tech_info=...,
        cleared=...,
        transaction_id=...,
        variable_monitoring_id=...,
    ) -> None: ...

@dataclass
class FirmwareType:
    location: str
    retrieve_date_time: str
    install_date_time: str | None = ...
    signing_certificate: str | None = ...
    signature: str | None = ...
    def __init__(
        self,
        location,
        retrieve_date_time,
        install_date_time=...,
        signing_certificate=...,
        signature=...,
    ) -> None: ...

@dataclass
class GetVariableDataType:
    component: ComponentType
    variable: VariableType
    attribute_type: enums.AttributeType | None = ...
    def __init__(self, component, variable, attribute_type=...) -> None: ...

@dataclass
class GetVariableResultType:
    attribute_status: enums.GetVariableStatusType
    component: ComponentType
    variable: VariableType
    attribute_type: enums.AttributeType | None = ...
    attribute_value: str | None = ...
    attribute_status_info: StatusInfoType | None = ...
    def __init__(
        self,
        attribute_status,
        component,
        variable,
        attribute_type=...,
        attribute_value=...,
        attribute_status_info=...,
    ) -> None: ...

@dataclass
class IdTokenType:
    id_token: str
    type: enums.IdTokenType
    additional_info: list[AdditionalInfoType] | None = ...
    def __init__(self, id_token, type, additional_info=...) -> None: ...

@dataclass
class MessageContentType:
    format: enums.MessageFormatType
    content: str
    language: str | None = ...
    def __init__(self, format, content, language=...) -> None: ...

@dataclass
class IdTokenInfoType:
    status: enums.AuthorizationStatusType
    cache_expiry_date_time: str | None = ...
    charging_priority: int | None = ...
    language_1: str | None = ...
    evse_id: list[int] | None = ...
    language_2: str | None = ...
    group_id_token: IdTokenType | None = ...
    personal_message: MessageContentType | None = ...
    def __init__(
        self,
        status,
        cache_expiry_date_time=...,
        charging_priority=...,
        language_1=...,
        evse_id=...,
        language_2=...,
        group_id_token=...,
        personal_message=...,
    ) -> None: ...

@dataclass
class AuthorizationData:
    id_token: IdTokenType
    id_token_info: IdTokenInfoType | None = ...
    def __init__(self, id_token, id_token_info=...) -> None: ...

@dataclass
class LogParametersType:
    remote_location: str
    oldest_timestamp: str | None = ...
    latest_timestamp: str | None = ...
    def __init__(
        self, remote_location, oldest_timestamp=..., latest_timestamp=...
    ) -> None: ...

@dataclass
class MessageInfoType:
    id: int
    priority: enums.MessagePriorityType
    message: MessageContentType
    state: enums.MessageStateType | None = ...
    start_date_time: str | None = ...
    end_date_time: str | None = ...
    transaction_id: str | None = ...
    display: ComponentType | None = ...
    def __init__(
        self,
        id,
        priority,
        message,
        state=...,
        start_date_time=...,
        end_date_time=...,
        transaction_id=...,
        display=...,
    ) -> None: ...

@dataclass
class SignedMeterValueType:
    signed_meter_data: str
    signing_method: str
    encoding_method: str
    public_key: str
    def __init__(
        self, signed_meter_data, signing_method, encoding_method, public_key
    ) -> None: ...

@dataclass
class UnitOfMeasureType:
    unit: str | None = ...
    multiplier: int | None = ...
    def __init__(self, unit=..., multiplier=...) -> None: ...

@dataclass
class SampledValueType:
    value: float
    context: enums.ReadingContextType | None = ...
    measurand: enums.MeasurandType | None = ...
    phase: enums.PhaseType | None = ...
    location: enums.LocationType | None = ...
    signed_meter_value: SignedMeterValueType | None = ...
    unit_of_measure: UnitOfMeasureType | None = ...
    def __init__(
        self,
        value,
        context=...,
        measurand=...,
        phase=...,
        location=...,
        signed_meter_value=...,
        unit_of_measure=...,
    ) -> None: ...

@dataclass
class MeterValueType:
    timestamp: str
    sampled_value: list[SampledValueType]
    def __init__(self, timestamp, sampled_value) -> None: ...

@dataclass
class ModemType:
    iccid: str | None = ...
    imsi: str | None = ...
    def __init__(self, iccid=..., imsi=...) -> None: ...

@dataclass
class VariableMonitoringType:
    id: int
    transaction: bool
    value: float
    type: enums.MonitorType
    severity: int
    def __init__(self, id, transaction, value, type, severity) -> None: ...

@dataclass
class MonitoringDataType:
    component: ComponentType
    variable: VariableType
    variable_monitoring: list[VariableMonitoringType]
    def __init__(self, component, variable, variable_monitoring) -> None: ...

@dataclass
class VPNType:
    server: str
    user: str
    password: str
    key: str
    type: enums.VPNType
    group: str | None = ...
    def __init__(self, server, user, password, key, type, group=...) -> None: ...

@dataclass
class NetworkConnectionProfileType:
    ocpp_version: enums.OCPPVersionType
    ocpp_transport: enums.OCPPTransportType
    ocpp_csms_url: str
    message_timeout: int
    security_profile: int
    ocpp_interface: enums.OCPPInterfaceType
    vpn: VPNType | None = ...
    apn: APNType | None = ...
    def __init__(
        self,
        ocpp_version,
        ocpp_transport,
        ocpp_csms_url,
        message_timeout,
        security_profile,
        ocpp_interface,
        vpn=...,
        apn=...,
    ) -> None: ...

@dataclass
class ChargingStationType:
    vendor_name: str
    model: str
    modem: ModemType | None = ...
    serial_number: str | None = ...
    firmware_version: str | None = ...
    def __init__(
        self, vendor_name, model, modem=..., serial_number=..., firmware_version=...
    ) -> None: ...

@dataclass
class OCSPRequestDataType:
    hash_algorithm: enums.HashAlgorithmType
    issuer_name_hash: str
    issuer_key_hash: str
    serial_number: str
    responder_url: str
    def __init__(
        self,
        hash_algorithm,
        issuer_name_hash,
        issuer_key_hash,
        serial_number,
        responder_url,
    ) -> None: ...

@dataclass
class VariableAttributeType:
    type: enums.AttributeType | None = ...
    value: str | None = ...
    mutability: enums.MutabilityType | None = ...
    persistent: bool | None = ...
    constant: bool | None = ...
    def __init__(
        self, type=..., value=..., mutability=..., persistent=..., constant=...
    ) -> None: ...

@dataclass
class VariableCharacteristicsType:
    data_type: enums.DataType
    supports_monitoring: bool
    unit: str | None = ...
    min_limit: float | None = ...
    max_limit: float | None = ...
    values_list: str | None = ...
    def __init__(
        self,
        data_type,
        supports_monitoring,
        unit=...,
        min_limit=...,
        max_limit=...,
        values_list=...,
    ) -> None: ...

@dataclass
class ReportDataType:
    component: ComponentType
    variable: VariableType
    variable_attribute: list[VariableAttributeType]
    variable_characteristics: VariableCharacteristicsType | None = ...
    def __init__(
        self, component, variable, variable_attribute, variable_characteristics=...
    ) -> None: ...

@dataclass
class SetMonitoringDataType:
    value: float
    type: enums.MonitorType
    severity: int
    component: ComponentType
    variable: VariableType
    id: int | None = ...
    transaction: bool | None = ...
    def __init__(
        self, value, type, severity, component, variable, id=..., transaction=...
    ) -> None: ...

@dataclass
class SetMonitoringResultType:
    status: enums.SetMonitoringStatusType
    type: enums.MonitorType
    severity: int
    component: ComponentType
    variable: VariableType
    id: int | None = ...
    status_info: StatusInfoType | None = ...
    def __init__(
        self, status, type, severity, component, variable, id=..., status_info=...
    ) -> None: ...

@dataclass
class SetVariableDataType:
    attribute_value: str
    component: ComponentType
    variable: VariableType
    attribute_type: enums.AttributeType | None = ...
    def __init__(
        self, attribute_value, component, variable, attribute_type=...
    ) -> None: ...

@dataclass
class SetVariableResultType:
    attribute_status: enums.SetVariableStatusType
    component: ComponentType
    variable: VariableType
    attribute_type: enums.AttributeType | None = ...
    attribute_status_info: StatusInfoType | None = ...
    def __init__(
        self,
        attribute_status,
        component,
        variable,
        attribute_type=...,
        attribute_status_info=...,
    ) -> None: ...

@dataclass
class TransactionType:
    transaction_id: str
    charging_state: enums.ChargingStateType | None = ...
    time_spent_charging: int | None = ...
    stopped_reason: enums.ReasonType | None = ...
    remote_start_id: int | None = ...
    def __init__(
        self,
        transaction_id,
        charging_state=...,
        time_spent_charging=...,
        stopped_reason=...,
        remote_start_id=...,
    ) -> None: ...
