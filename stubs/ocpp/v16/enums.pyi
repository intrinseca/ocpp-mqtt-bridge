from enum import StrEnum

class Action(StrEnum):
    def __init__(self, *args, **kwargs) -> None: ...
    Authorize = "Authorize"
    BootNotification = "BootNotification"
    CancelReservation = "CancelReservation"
    CertificateSigned = "CertificateSigned"
    ChangeAvailability = "ChangeAvailability"
    ChangeConfiguration = "ChangeConfiguration"
    ClearCache = "ClearCache"
    ClearChargingProfile = "ClearChargingProfile"
    DataTransfer = "DataTransfer"
    DeleteCertificate = "DeleteCertificate"
    DiagnosticsStatusNotification = "DiagnosticsStatusNotification"
    ExtendedTriggerMessage = "ExtendedTriggerMessage"
    FirmwareStatusNotification = "FirmwareStatusNotification"
    GetCompositeSchedule = "GetCompositeSchedule"
    GetConfiguration = "GetConfiguration"
    GetDiagnostics = "GetDiagnostics"
    GetInstalledCertificateIds = "GetInstalledCertificateIds"
    GetLocalListVersion = "GetLocalListVersion"
    GetLog = "GetLog"
    Heartbeat = "Heartbeat"
    InstallCertificate = "InstallCertificate"
    LogStatusNotification = "LogStatusNotification"
    MeterValues = "MeterValues"
    RemoteStartTransaction = "RemoteStartTransaction"
    RemoteStopTransaction = "RemoteStopTransaction"
    ReserveNow = "ReserveNow"
    Reset = "Reset"
    SecurityEventNotification = "SecurityEventNotification"
    SendLocalList = "SendLocalList"
    SetChargingProfile = "SetChargingProfile"
    SignCertificate = "SignCertificate"
    SignedFirmwareStatusNotification = "SignedFirmwareStatusNotification"
    SignedUpdateFirmware = "SignedUpdateFirmware"
    StartTransaction = "StartTransaction"
    StatusNotification = "StatusNotification"
    StopTransaction = "StopTransaction"
    TriggerMessage = "TriggerMessage"
    UnlockConnector = "UnlockConnector"
    UpdateFirmware = "UpdateFirmware"
    authorize = "Authorize"
    boot_notification = "BootNotification"
    cancel_reservation = "CancelReservation"
    certificate_signed = "CertificateSigned"
    change_availability = "ChangeAvailability"
    change_configuration = "ChangeConfiguration"
    clear_cache = "ClearCache"
    clear_charging_profile = "ClearChargingProfile"
    data_transfer = "DataTransfer"
    delete_certificate = "DeleteCertificate"
    diagnostics_status_notification = "DiagnosticsStatusNotification"
    extended_trigger_message = "ExtendedTriggerMessage"
    firmware_status_notification = "FirmwareStatusNotification"
    get_composite_schedule = "GetCompositeSchedule"
    get_configuration = "GetConfiguration"
    get_diagnostics = "GetDiagnostics"
    get_installed_certificate_ids = "GetInstalledCertificateIds"
    get_local_list_version = "GetLocalListVersion"
    get_log = "GetLog"
    heartbeat = "Heartbeat"
    install_certificate = "InstallCertificate"
    log_status_notification = "LogStatusNotification"
    meter_values = "MeterValues"
    remote_start_transaction = "RemoteStartTransaction"
    remote_stop_transaction = "RemoteStopTransaction"
    reserve_now = "ReserveNow"
    reset = "Reset"
    security_event_notification = "SecurityEventNotification"
    send_local_list = "SendLocalList"
    set_charging_profile = "SetChargingProfile"
    sign_certificate = "SignCertificate"
    signed_firmware_status_notification = "SignedFirmwareStatusNotification"
    signed_update_firmware = "SignedUpdateFirmware"
    start_transaction = "StartTransaction"
    status_notification = "StatusNotification"
    stop_transaction = "StopTransaction"
    trigger_message = "TriggerMessage"
    unlock_connector = "UnlockConnector"
    update_firmware = "UpdateFirmware"

class AuthorizationStatus(StrEnum):
    accepted = "Accepted"
    blocked = "Blocked"
    expired = "Expired"
    invalid = "Invalid"
    concurrent_tx = "ConcurrentTx"

class AvailabilityStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"

class AvailabilityType(StrEnum):
    inoperative = "Inoperative"
    operative = "Operative"

class CancelReservationStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class CertificateSignedStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class CertificateStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"

class CertificateUse(StrEnum):
    central_system_root_certificate = "CentralSystemRootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"

class ChargePointErrorCode(StrEnum):
    connector_lock_failure = "ConnectorLockFailure"
    ev_communication_error = "EVCommunicationError"
    ground_failure = "GroundFailure"
    high_temperature = "HighTemperature"
    internal_error = "InternalError"
    local_list_conflict = "LocalListConflict"
    no_error = "NoError"
    other_error = "OtherError"
    over_current_failure = "OverCurrentFailure"
    over_voltage = "OverVoltage"
    power_meter_failure = "PowerMeterFailure"
    power_switch_failure = "PowerSwitchFailure"
    reader_failure = "ReaderFailure"
    reset_failure = "ResetFailure"
    under_voltage = "UnderVoltage"
    weak_signal = "WeakSignal"

class ChargePointStatus(StrEnum):
    available = "Available"
    preparing = "Preparing"
    charging = "Charging"
    suspended_evse = "SuspendedEVSE"
    suspended_ev = "SuspendedEV"
    finishing = "Finishing"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"

class ChargingProfileKindType(StrEnum):
    absolute = "Absolute"
    recurring = "Recurring"
    relative = "Relative"

class ChargingProfilePurposeType(StrEnum):
    charge_point_max_profile = "ChargePointMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"

class ChargingProfileStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"

class ChargingRateUnitType(StrEnum):
    watts = "W"
    amps = "A"

class CiStringType(int):
    ci_string_20: int
    ci_string_25: int
    ci_string_50: int
    ci_string_255: int
    ci_string_500: int

class ClearCacheStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class ClearChargingProfileStatus(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"

class ConfigurationStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    reboot_required = "RebootRequired"
    not_supported = "NotSupported"

class ConfigurationKey(StrEnum):
    allow_offline_tx_for_unknown_id = "AllowOfflineTxForUnknownId"
    authorization_cache_enabled = "AuthorizationCacheEnabled"
    authorize_remote_tx_requests = "AuthorizeRemoteTxRequests"
    blink_repeat = "BlinkRepeat"
    clock_aligned_data_interval = "ClockAlignedDataInterval"
    connection_time_out = "ConnectionTimeOut"
    connector_phase_rotation = "ConnectorPhaseRotation"
    connector_phase_rotation_max_length = "ConnectorPhaseRotationMaxLength"
    get_configuration_max_keys = "GetConfigurationMaxKeys"
    heartbeat_interval = "HeartbeatInterval"
    light_intensity = "LightIntensity"
    local_authorize_offline = "LocalAuthorizeOffline"
    local_pre_authorize = "LocalPreAuthorize"
    max_energy_on_invalid_id = "MaxEnergyOnInvalidId"
    meter_values_aligned_data = "MeterValuesAlignedData"
    meter_values_aligned_data_max_length = "MeterValuesAlignedDataMaxLength"
    meter_values_sampled_data = "MeterValuesSampledData"
    meter_values_sampled_data_max_length = "MeterValuesSampledDataMaxLength"
    meter_value_sample_interval = "MeterValueSampleInterval"
    minimum_status_duration = "MinimumStatusDuration"
    number_of_connectors = "NumberOfConnectors"
    reset_retries = "ResetRetries"
    stop_transaction_on_ev_side_disconnect = "StopTransactionOnEVSideDisconnect"
    stop_transaction_on_invalid_id = "StopTransactionOnInvalidId"
    stop_txn_aligned_data = "StopTxnAlignedData"
    stop_txn_aligned_data_max_length = "StopTxnAlignedDataMaxLength"
    stop_txn_sampled_data = "StopTxnSampledData"
    stop_txn_sampled_data_max_length = "StopTxnSampledDataMaxLength"
    supported_feature_profiles = "SupportedFeatureProfiles"
    supported_feature_profiles_max_length = "SupportedFeatureProfilesMaxLength"
    transaction_message_attempts = "TransactionMessageAttempts"
    transaction_message_retry_interval = "TransactionMessageRetryInterval"
    unlock_connector_on_ev_side_disconnect = "UnlockConnectorOnEVSideDisconnect"
    web_socket_ping_interval = "WebSocketPingInterval"
    local_auth_list_enabled = "LocalAuthListEnabled"
    local_auth_list_max_length = "LocalAuthListMaxLength"
    send_local_list_max_length = "SendLocalListMaxLength"
    reserve_connector_zero_supported = "ReserveConnectorZeroSupported"
    charge_profile_max_stack_level = "ChargeProfileMaxStackLevel"
    charging_schedule_allowed_charging_rate_unit = (
        "ChargingScheduleAllowedChargingRateUnit"
    )
    charging_schedule_max_periods = "ChargingScheduleMaxPeriods"
    connector_switch_3to1_phase_supported = "ConnectorSwitch3to1PhaseSupported"
    max_charging_profiles_installed = "MaxChargingProfilesInstalled"
    central_contract_validation_allowed = "CentralContractValidationAllowed"
    certificate_signed_max_chain_size = "CertificateSignedMaxChainSize"
    cert_signing_wait_minimum = "CertSigningWaitMinimum"
    cert_signing_repeat_times = "CertSigningRepeatTimes"
    certificate_store_max_length = "CertificateStoreMaxLength"
    contract_validation_offline = "ContractValidationOffline"
    iso_15118_pnc_enabled = "ISO15118PnCEnabled"
    additional_root_certificate_check = "AdditionalRootCertificateCheck"
    authorization_key = "AuthorizationKey"
    cpo_name = "CpoName"
    security_profile = "SecurityProfile"

class DataTransferStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"

class DeleteCertificateStatus(StrEnum):
    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"

class DiagnosticsStatus(StrEnum):
    idle = "Idle"
    uploaded = "Uploaded"
    upload_failed = "UploadFailed"
    uploading = "Uploading"

class FirmwareStatus(StrEnum):
    downloaded = "Downloaded"
    download_failed = "DownloadFailed"
    downloading = "Downloading"
    idle = "Idle"
    installation_failed = "InstallationFailed"
    installing = "Installing"
    installed = "Installed"
    download_scheduled = "DownloadScheduled"
    download_paused = "DownloadPaused"
    install_rebooting = "InstallRebooting"
    install_scheduled = "InstallScheduled"
    install_verification_failed = "InstallVerificationFailed"
    invalid_signature = "InvalidSignature"
    signature_verified = "SignatureVerified"

class GenericStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class GetCompositeScheduleStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class GetInstalledCertificateStatus(StrEnum):
    accepted = "Accepted"
    not_found = "NotFound"

class HashAlgorithm(StrEnum):
    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"

class Location(StrEnum):
    inlet = "Inlet"
    outlet = "Outlet"
    body = "Body"
    cable = "Cable"
    ev = "EV"

class Log(StrEnum):
    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"

class LogStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"

class Measurand(StrEnum):
    current_export = "Current.Export"
    current_import = "Current.Import"
    current_offered = "Current.Offered"
    energy_active_export_register = "Energy.Active.Export.Register"
    energy_active_import_register = "Energy.Active.Import.Register"
    energy_reactive_export_register = "Energy.Reactive.Export.Register"
    energy_reactive_import_register = "Energy.Reactive.Import.Register"
    energy_active_export_interval = "Energy.Active.Export.Interval"
    energy_active_import_interval = "Energy.Active.Import.Interval"
    energy_reactive_export_interval = "Energy.Reactive.Export.Interval"
    energy_reactive_import_interval = "Energy.Reactive.Import.Interval"
    frequency = "Frequency"
    power_active_export = "Power.Active.Export"
    power_active_import = "Power.Active.Import"
    power_factor = "Power.Factor"
    power_offered = "Power.Offered"
    power_reactive_export = "Power.Reactive.Export"
    power_reactive_import = "Power.Reactive.Import"
    rpm = "RPM"
    soc = "SoC"
    temperature = "Temperature"
    voltage = "Voltage"

class MessageTrigger(StrEnum):
    boot_notification = "BootNotification"
    firmware_status_notification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meter_values = "MeterValues"
    status_notification = "StatusNotification"
    diagnostics_status_notification = "DiagnosticsStatusNotification"
    log_status_notification = "LogStatusNotification"
    sign_charge_point_certificate = "SignChargePointCertificate"

class Phase(StrEnum):
    l1 = "L1"
    l2 = "L2"
    l3 = "L3"
    n = "N"
    l1_n = "L1-N"
    l2_n = "L2-N"
    l3_n = "L3-N"
    l1_l2 = "L1-L2"
    l2_l3 = "L2-L3"
    l3_l1 = "L3-L1"

class ReadingContext(StrEnum):
    interruption_begin = "Interruption.Begin"
    interruption_end = "Interruption.End"
    other = "Other"
    sample_clock = "Sample.Clock"
    sample_periodic = "Sample.Periodic"
    transaction_begin = "Transaction.Begin"
    transaction_end = "Transaction.End"
    trigger = "Trigger"

class Reason(StrEnum):
    emergency_stop = "EmergencyStop"
    ev_disconnected = "EVDisconnected"
    hard_reset = "HardReset"
    local = "Local"
    other = "Other"
    power_loss = "PowerLoss"
    reboot = "Reboot"
    remote = "Remote"
    soft_reset = "SoftReset"
    unlock_command = "UnlockCommand"
    de_authorized = "DeAuthorized"

class RecurrencyKind(StrEnum):
    daily = "Daily"
    weekly = "Weekly"

class RegistrationStatus(StrEnum):
    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"

class RemoteStartStopStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class ReservationStatus(StrEnum):
    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"

class ResetStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class ResetType(StrEnum):
    hard = "Hard"
    soft = "Soft"

class TriggerMessageStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"

class UnitOfMeasure(StrEnum):
    wh = "Wh"
    kwh = "kWh"
    varh = "varh"
    kvarh = "kvarh"
    w = "W"
    kw = "kW"
    va = "VA"
    kva = "kVA"
    var = "var"
    kvar = "kvar"
    a = "A"
    v = "V"
    celsius = "Celsius"
    fahrenheit = "Fahrenheit"
    k = "K"
    percent = "Percent"

class UnlockStatus(StrEnum):
    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"
    not_supported = "NotSupported"

class UpdateFirmwareStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"

class UploadLogStatus(StrEnum):
    bad_message = "BadMessage"
    idle = "Idle"
    not_supported_operation = "NotSupportedOperation"
    permission_denied = "PermissionDenied"
    uploaded = "Uploaded"
    upload_failure = "UploadFailure"
    uploading = "Uploading"

class UpdateStatus(StrEnum):
    accepted = "Accepted"
    failed = "Failed"
    not_supported = "NotSupported"
    version_mismatch = "VersionMismatch"

class UpdateType(StrEnum):
    differential = "Differential"
    full = "Full"

class ValueFormat(StrEnum):
    raw = "Raw"
    signed_data = "SignedData"
