from dataclasses import dataclass
from ocpp.v16.enums import AuthorizationStatus as AuthorizationStatus, ChargingProfileKindType as ChargingProfileKindType, ChargingProfilePurposeType as ChargingProfilePurposeType, ChargingRateUnitType as ChargingRateUnitType, CiStringType as CiStringType, HashAlgorithm as HashAlgorithm, Location as Location, Measurand as Measurand, Phase as Phase, ReadingContext as ReadingContext, RecurrencyKind as RecurrencyKind, UnitOfMeasure as UnitOfMeasure, ValueFormat as ValueFormat

@dataclass
class IdTagInfo:
    status: AuthorizationStatus
    parent_id_tag: str | None = ...
    expiry_date: str | None = ...
    def __init__(self, status, parent_id_tag=..., expiry_date=...) -> None: ...

@dataclass
class AuthorizationData:
    id_tag: str
    id_tag_info: IdTagInfo | None = ...
    def __init__(self, id_tag, id_tag_info=...) -> None: ...

@dataclass
class ChargingSchedulePeriod:
    start_period: int
    limit: float
    number_phases: int | None = ...
    def __init__(self, start_period, limit, number_phases=...) -> None: ...

@dataclass
class ChargingSchedule:
    charging_rate_unit: ChargingRateUnitType
    charging_schedule_period: list[ChargingSchedulePeriod]
    duration: int | None = ...
    start_schedule: str | None = ...
    min_charging_rate: float | None = ...
    def __init__(self, charging_rate_unit, charging_schedule_period, duration=..., start_schedule=..., min_charging_rate=...) -> None: ...

@dataclass
class ChargingProfile:
    charging_profile_id: int
    stack_level: int
    charging_profile_purpose: ChargingProfilePurposeType
    charging_profile_kind: ChargingProfileKindType
    charging_schedule: ChargingSchedule
    transaction_id: int | None = ...
    recurrency_kind: RecurrencyKind | None = ...
    valid_from: str | None = ...
    valid_to: str | None = ...
    def __init__(self, charging_profile_id, stack_level, charging_profile_purpose, charging_profile_kind, charging_schedule, transaction_id=..., recurrency_kind=..., valid_from=..., valid_to=...) -> None: ...

@dataclass
class KeyValue:
    key: str
    readonly: bool
    value: str | None = ...
    def __post_init__(self) -> None: ...
    def __init__(self, key, readonly, value=...) -> None: ...

@dataclass
class SampledValue:
    value: str
    context: ReadingContext | None = ...
    format: ValueFormat | None = ...
    measurand: Measurand | None = ...
    phase: Phase | None = ...
    location: Location | None = ...
    unit: UnitOfMeasure | None = ...
    def __init__(self, value, context=..., format=..., measurand=..., phase=..., location=..., unit=...) -> None: ...

@dataclass
class MeterValue:
    timestamp: str
    sampled_value: list[SampledValue]
    def __init__(self, timestamp, sampled_value) -> None: ...

@dataclass
class CertificateHashData:
    hash_algorithm: HashAlgorithm
    issuer_name_hash: str
    issuer_key_hash: str
    serial_number: str
    def __init__(self, hash_algorithm, issuer_name_hash, issuer_key_hash, serial_number) -> None: ...

@dataclass
class Firmware:
    location: str
    retrieve_date_time: str
    signing_certificate: str
    install_date_time: str | None = ...
    signature: str | None = ...
    def __init__(self, location, retrieve_date_time, signing_certificate, install_date_time=..., signature=...) -> None: ...

@dataclass
class LogParameters:
    remote_location: str
    oldest_timestamp: str | None = ...
    latest_timestamp: str | None = ...
    def __init__(self, remote_location, oldest_timestamp=..., latest_timestamp=...) -> None: ...
