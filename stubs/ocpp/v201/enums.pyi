from enum import StrEnum

class Action(StrEnum):
    def __init__(self, *args, **kwargs) -> None: ...
    Authorize = "Authorize"
    BootNotification = "BootNotification"
    CancelReservation = "CancelReservation"
    CertificateSigned = "CertificateSigned"
    ChangeAvailability = "ChangeAvailability"
    ClearCache = "ClearCache"
    ClearChargingProfile = "ClearChargingProfile"
    ClearDisplayMessage = "ClearDisplayMessage"
    ClearedChargingLimit = "ClearedChargingLimit"
    ClearVariableMonitoring = "ClearVariableMonitoring"
    CostUpdated = "CostUpdated"
    CustomerInformation = "CustomerInformation"
    DataTransfer = "DataTransfer"
    DeleteCertificate = "DeleteCertificate"
    FirmwareStatusNotification = "FirmwareStatusNotification"
    Get15118EVCertificate = "Get15118EVCertificate"
    GetBaseReport = "GetBaseReport"
    GetCertificateStatus = "GetCertificateStatus"
    GetChargingProfiles = "GetChargingProfiles"
    GetCompositeSchedule = "GetCompositeSchedule"
    GetDisplayMessages = "GetDisplayMessages"
    GetInstalledCertificateIds = "GetInstalledCertificateIds"
    GetLocalListVersion = "GetLocalListVersion"
    GetLog = "GetLog"
    GetMonitoringReport = "GetMonitoringReport"
    GetReport = "GetReport"
    GetTransactionStatus = "GetTransactionStatus"
    GetVariables = "GetVariables"
    Heartbeat = "Heartbeat"
    InstallCertificate = "InstallCertificate"
    LogStatusNotification = "LogStatusNotification"
    MeterValues = "MeterValues"
    NotifyChargingLimit = "NotifyChargingLimit"
    NotifyCustomerInformation = "NotifyCustomerInformation"
    NotifyDisplayMessages = "NotifyDisplayMessages"
    NotifyEVChargingNeeds = "NotifyEVChargingNeeds"
    NotifyEVChargingSchedule = "NotifyEVChargingSchedule"
    NotifyEvent = "NotifyEvent"
    NotifyMonitoringReport = "NotifyMonitoringReport"
    NotifyReport = "NotifyReport"
    PublishFirmware = "PublishFirmware"
    PublishFirmwareStatusNotification = "PublishFirmwareStatusNotification"
    ReportChargingProfiles = "ReportChargingProfiles"
    RequestStartTransaction = "RequestStartTransaction"
    RequestStopTransaction = "RequestStopTransaction"
    ReservationStatusUpdate = "ReservationStatusUpdate"
    ReserveNow = "ReserveNow"
    Reset = "Reset"
    SecurityEventNotification = "SecurityEventNotification"
    SendLocalList = "SendLocalList"
    SetChargingProfile = "SetChargingProfile"
    SetDisplayMessage = "SetDisplayMessage"
    SetMonitoringBase = "SetMonitoringBase"
    SetMonitoringLevel = "SetMonitoringLevel"
    SetNetworkProfile = "SetNetworkProfile"
    SetVariableMonitoring = "SetVariableMonitoring"
    SetVariables = "SetVariables"
    SignCertificate = "SignCertificate"
    StatusNotification = "StatusNotification"
    TransactionEvent = "TransactionEvent"
    TriggerMessage = "TriggerMessage"
    UnlockConnector = "UnlockConnector"
    UnpublishFirmware = "UnpublishFirmware"
    UpdateFirmware = "UpdateFirmware"
    authorize = "Authorize"
    boot_notification = "BootNotification"
    cancel_reservation = "CancelReservation"
    certificate_signed = "CertificateSigned"
    change_availability = "ChangeAvailability"
    clear_cache = "ClearCache"
    clear_charging_profile = "ClearChargingProfile"
    clear_display_message = "ClearDisplayMessage"
    cleared_charging_limit = "ClearedChargingLimit"
    clear_variable_monitoring = "ClearVariableMonitoring"
    cost_updated = "CostUpdated"
    customer_information = "CustomerInformation"
    data_transfer = "DataTransfer"
    delete_certificate = "DeleteCertificate"
    firmware_status_notification = "FirmwareStatusNotification"
    get_15118_ev_certificate = "Get15118EVCertificate"
    get_base_report = "GetBaseReport"
    get_certificate_status = "GetCertificateStatus"
    get_charging_profiles = "GetChargingProfiles"
    get_composite_schedule = "GetCompositeSchedule"
    get_display_messages = "GetDisplayMessages"
    get_installed_certificate_ids = "GetInstalledCertificateIds"
    get_local_list_version = "GetLocalListVersion"
    get_log = "GetLog"
    get_monitoring_report = "GetMonitoringReport"
    get_report = "GetReport"
    get_transaction_status = "GetTransactionStatus"
    get_variables = "GetVariables"
    heartbeat = "Heartbeat"
    install_certificate = "InstallCertificate"
    log_status_notification = "LogStatusNotification"
    meter_values = "MeterValues"
    notify_charging_limit = "NotifyChargingLimit"
    notify_customer_information = "NotifyCustomerInformation"
    notify_display_messages = "NotifyDisplayMessages"
    notify_ev_charging_needs = "NotifyEVChargingNeeds"
    notify_ev_charging_schedule = "NotifyEVChargingSchedule"
    notify_event = "NotifyEvent"
    notify_monitoring_report = "NotifyMonitoringReport"
    notify_report = "NotifyReport"
    publish_firmware = "PublishFirmware"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"
    report_charging_profiles = "ReportChargingProfiles"
    request_start_transaction = "RequestStartTransaction"
    request_stop_transaction = "RequestStopTransaction"
    reservation_status_update = "ReservationStatusUpdate"
    reserve_now = "ReserveNow"
    reset = "Reset"
    security_event_notification = "SecurityEventNotification"
    send_local_list = "SendLocalList"
    set_charging_profile = "SetChargingProfile"
    set_display_message = "SetDisplayMessage"
    set_monitoring_base = "SetMonitoringBase"
    set_monitoring_level = "SetMonitoringLevel"
    set_network_profile = "SetNetworkProfile"
    set_variable_monitoring = "SetVariableMonitoring"
    set_variables = "SetVariables"
    sign_certificate = "SignCertificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"
    trigger_message = "TriggerMessage"
    unlock_connector = "UnlockConnector"
    unpublish_firmware = "UnpublishFirmware"
    update_firmware = "UpdateFirmware"

class APNAuthenticationType(StrEnum):
    chap = "CHAP"
    none = "NONE"
    pap = "PAP"
    auto = "AUTO"

class AttributeType(StrEnum):
    actual = "Actual"
    target = "Target"
    min_set = "MinSet"
    max_set = "MaxSet"

class AuthorizationStatusType(StrEnum):
    accepted = "Accepted"
    blocked = "Blocked"
    concurrent_tx = "ConcurrentTx"
    expired = "Expired"
    invalid = "Invalid"
    no_credit = "NoCredit"
    not_allowed_type_evse = "NotAllowedTypeEVSE"
    not_at_this_location = "NotAtThisLocation"
    not_at_this_time = "NotAtThisTime"
    unknown = "Unknown"

class AuthorizeCertificateStatusType(StrEnum):
    accepted = "Accepted"
    signature_error = "SignatureError"
    certificate_expired = "CertificateExpired"
    certificate_revoked = "CertificateRevoked"
    no_certificate_available = "NoCertificateAvailable"
    cert_chain_error = "CertChainError"
    contract_cancelled = "ContractCancelled"

class BootReasonType(StrEnum):
    application_reset = "ApplicationReset"
    firmware_update = "FirmwareUpdate"
    local_reset = "LocalReset"
    power_up = "PowerUp"
    remote_reset = "RemoteReset"
    scheduled_reset = "ScheduledReset"
    triggered = "Triggered"
    unknown = "Unknown"
    watchdog = "Watchdog"

class CancelReservationStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class CertificateActionType(StrEnum):
    install = "Install"
    update = "Update"

class CertificateSignedStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class CertificateSigningUseType(StrEnum):
    charging_station_certificate = "ChargingStationCertificate"
    v2g_certificate = "V2GCertificate"

class ChangeAvailabilityStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"

class ChargingLimitSourceType(StrEnum):
    ems = "EMS"
    other = "Other"
    so = "SO"
    cso = "CSO"

class ChargingProfileKindType(StrEnum):
    absolute = "Absolute"
    recurring = "Recurring"
    relative = "Relative"

class ChargingProfilePurposeType(StrEnum):
    charging_station_external_constraints = "ChargingStationExternalConstraints"
    charging_station_max_profile = "ChargingStationMaxProfile"
    tx_default_profile = "TxDefaultProfile"
    tx_profile = "TxProfile"

class ChargingProfileStatus(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class ChargingRateUnitType(StrEnum):
    watts = "W"
    amps = "A"

class ChargingStateType(StrEnum):
    charging = "Charging"
    ev_connected = "EVConnected"
    suspended_ev = "SuspendedEV"
    suspended_evse = "SuspendedEVSE"
    idle = "Idle"

class ClearCacheStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class ClearChargingProfileStatusType(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"

class ClearMessageStatusType(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"

class ClearMonitoringStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_found = "NotFound"

class ComponentCriterionType(StrEnum):
    active = "Active"
    available = "Available"
    enabled = "Enabled"
    problem = "Problem"

class ConnectorStatusType(StrEnum):
    available = "Available"
    occupied = "Occupied"
    reserved = "Reserved"
    unavailable = "Unavailable"
    faulted = "Faulted"

class ConnectorType(StrEnum):
    c_ccs1 = "cCCS1"
    c_ccs2 = "cCCS2"
    c_chao_ji = "cChaoJi"
    c_g105 = "cG105"
    c_gbt = "cGBT"
    c_tesla = "cTesla"
    c_type1 = "cType1"
    c_type2 = "cType2"
    s309_1p_16a = "s309-1P-16A"
    s309_1p_32a = "s309-1P-32A"
    s309_3p_16a = "s309-3P-16A"
    s309_3p_32a = "s309-3P-32A"
    s_bs1361 = "sBS1361"
    s_cee_7_7 = "sCEE-7-7"
    s_type2 = "sType2"
    s_type3 = "sType3"
    opp_charge = "OppCharge"
    other_1ph_max_16a = "Other1PhMax16A"
    other_1ph_over_16a = "Other1PhOver16A"
    other_3ph = "Other3Ph"
    pan = "Pan"
    w_inductive = "wInductive"
    w_resonant = "wResonant"
    undetermined = "Undetermined"
    unknown = "Unknown"

class CostKindType(StrEnum):
    carbon_dioxide_emission = "CarbonDioxideEmission"
    relative_price_percentage = "RelativePricePercentage"
    renewable_generation_percentage = "RenewableGenerationPercentage"

class CustomerInformationStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    invalid = "Invalid"

class DataTransferStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_message_id = "UnknownMessageId"
    unknown_vendor_id = "UnknownVendorId"

class DataType(StrEnum):
    string = "string"
    decimal = "decimal"
    integer = "integer"
    date_time = "dateTime"
    boolean = "boolean"
    option_list = "OptionList"
    sequence_list = "SequenceList"
    member_list = "MemberList"
    password_string = "passwordString"

class DeleteCertificateStatusType(StrEnum):
    accepted = "Accepted"
    failed = "Failed"
    not_found = "NotFound"

class DisplayMessageStatusType(StrEnum):
    accepted = "Accepted"
    not_supported_message_format = "NotSupportedMessageFormat"
    rejected = "Rejected"
    not_supported_priority = "NotSupportedPriority"
    not_supported_state = "NotSupportedState"
    unknown_transaction = "UnknownTransaction"

class EnergyTransferModeType(StrEnum):
    dc = "DC"
    ac_single_phase = "AC_single_phase"
    ac_two_phase = "AC_two_phase"
    ac_three_phase = "AC_three_phase"

class EventNotificationType(StrEnum):
    hard_wired_notification = "HardWiredNotification"
    hard_wired_monitor = "HardWiredMonitor"
    preconfigured_monitor = "PreconfiguredMonitor"
    custom_monitor = "CustomMonitor"

class EventTriggerType(StrEnum):
    alerting = "Alerting"
    delta = "Delta"
    periodic = "Periodic"

class FirmwareStatusType(StrEnum):
    downloaded = "Downloaded"
    download_failed = "DownloadFailed"
    downloading = "Downloading"
    download_scheduled = "DownloadScheduled"
    download_paused = "DownloadPaused"
    idle = "Idle"
    installation_failed = "InstallationFailed"
    installing = "Installing"
    installed = "Installed"
    install_rebooting = "InstallRebooting"
    install_scheduled = "InstallScheduled"
    install_verification_failed = "InstallVerificationFailed"
    invalid_signature = "InvalidSignature"
    signature_verified = "SignatureVerified"

class GenericDeviceModelStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_supported = "NotSupported"
    empty_result_set = "EmptyResultSet"

class GenericStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class GetCertificateIdUseType(StrEnum):
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    v2g_certificate_chain = "V2GCertificateChain"
    manufacturer_root_certificate = "ManufacturerRootCertificate"

class GetCertificateStatusType(StrEnum):
    accepted = "Accepted"
    failed = "Failed"

class GetChargingProfileStatusType(StrEnum):
    accepted = "Accepted"
    no_profiles = "NoProfiles"

class GetDisplayMessagesStatusType(StrEnum):
    accepted = "Accepted"
    unknown = "Unknown"

class GetInstalledCertificateStatusType(StrEnum):
    accepted = "Accepted"
    notFound = "NotFound"

class GetVariableStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"

class HashAlgorithmType(StrEnum):
    sha256 = "SHA256"
    sha384 = "SHA384"
    sha512 = "SHA512"

class IdTokenType(StrEnum):
    central = "Central"
    e_maid = "eMAID"
    iso14443 = "ISO14443"
    iso15693 = "ISO15693"
    key_code = "KeyCode"
    local = "Local"
    mac_address = "MacAddress"
    no_authorization = "NoAuthorization"

class InstallCertificateStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"

class InstallCertificateUseType(StrEnum):
    v2g_root_certificate = "V2GRootCertificate"
    mo_root_certificate = "MORootCertificate"
    csms_root_certificate = "CSMSRootCertificate"
    manufacturer_root_certificate = "ManufacturerRootCertificate"

class Iso15118EVCertificateStatusType(StrEnum):
    accepted = "Accepted"
    failed = "Failed"

class LocationType(StrEnum):
    body = "Body"
    cable = "Cable"
    ev = "EV"
    inlet = "Inlet"
    outlet = "Outlet"

class LogType(StrEnum):
    diagnostics_log = "DiagnosticsLog"
    security_log = "SecurityLog"

class LogStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"

class MeasurandType(StrEnum):
    current_export = "Current.Export"
    current_import = "Current.Import"
    current_offered = "Current.Offered"
    energy_active_export_register = "Energy.Active.Export.Register"
    energy_active_import_register = "Energy.Active.Import.Register"
    energy_reactive_export_register = "Energy.Reactive.Export.Register"
    energy_reactive_import_register = "Energy.Reactive.Import.Register"
    energy_active_export_interval = "Energy.Active.Export.Interval"
    energy_active_import_interval = "Energy.Active.Import.Interval"
    energy_active_net = "Energy.Active.Net"
    energy_reactive_export_interval = "Energy.Reactive.Export.Interval"
    energy_reactive_import_interval = "Energy.Reactive.Import.Interval"
    energy_reactive_net = "Energy.Reactive.Net"
    energy_apparent_net = "Energy.Apparent.Net"
    energy_apparent_import = "Energy.Apparent.Import"
    energy_apparent_export = "Energy.Apparent.Export"
    frequency = "Frequency"
    power_active_export = "Power.Active.Export"
    power_active_import = "Power.Active.Import"
    power_factor = "Power.Factor"
    power_offered = "Power.Offered"
    power_reactive_export = "Power.Reactive.Export"
    power_reactive_import = "Power.Reactive.Import"
    soc = "SoC"
    voltage = "Voltage"

class MessageFormatType(StrEnum):
    ascii = "ASCII"
    html = "HTML"
    uri = "URI"
    utf8 = "UTF8"

class MessagePriorityType(StrEnum):
    always_front = "AlwaysFront"
    in_front = "InFront"
    normal_cycle = "NormalCycle"

class MessageStateType(StrEnum):
    charging = "Charging"
    faulted = "Faulted"
    idle = "Idle"

class MessageTriggerType(StrEnum):
    boot_notification = "BootNotification"
    log_status_notification = "LogStatusNotification"
    firmware_status_notification = "FirmwareStatusNotification"
    heartbeat = "Heartbeat"
    meter_values = "MeterValues"
    sign_charging_station_certificate = "SignChargingStationCertificate"
    sign_v2g_certificate = "SignV2GCertificate"
    status_notification = "StatusNotification"
    transaction_event = "TransactionEvent"
    sign_combined_certificate = "SignCombinedCertificate"
    publish_firmware_status_notification = "PublishFirmwareStatusNotification"

class MonitorType(StrEnum):
    upper_threshold = "UpperThreshold"
    lower_threshold = "LowerThreshold"
    delta = "Delta"
    periodic = "Periodic"
    periodic_clock_aligned = "PeriodicClockAligned"

class MonitorBaseType(StrEnum):
    all = "All"
    factory_default = "FactoryDefault"
    hard_wired_only = "HardWiredOnly"

class MonitoringCriterionType(StrEnum):
    threshold_monitoring = "ThresholdMonitoring"
    delta_monitoring = "DeltaMonitoring"
    periodic_monitoring = "PeriodicMonitoring"

class MutabilityType(StrEnum):
    read_only = "ReadOnly"
    write_only = "WriteOnly"
    read_write = "ReadWrite"

class NotifyEVChargingNeedsStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    processing = "Processing"

class OCPPInterfaceType(StrEnum):
    wired0 = "Wired0"
    wired1 = "Wired1"
    wired2 = "Wired2"
    wired3 = "Wired3"
    wireless0 = "Wireless0"
    wireless1 = "Wireless1"
    wireless2 = "Wireless2"
    wireless3 = "Wireless3"

class OCPPTransportType(StrEnum):
    json = "JSON"
    soap = "SOAP"

class OCPPVersionType(StrEnum):
    ocpp12 = "OCPP12"
    ocpp15 = "OCPP15"
    ocpp16 = "OCPP16"
    ocpp20 = "OCPP20"

class OperationalStatusType(StrEnum):
    inoperative = "Inoperative"
    operative = "Operative"

class PhaseType(StrEnum):
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

class PublishFirmwareStatusType(StrEnum):
    idle = "Idle"
    download_scheduled = "DownloadScheduled"
    downloading = "Downloading"
    downloaded = "Downloaded"
    published = "Published"
    download_failed = "DownloadFailed"
    download_paused = "DownloadPaused"
    invalid_checksum = "InvalidChecksum"
    checksum_verified = "ChecksumVerified"
    publish_failed = "PublishFailed"

class ReadingContextType(StrEnum):
    interruption_begin = "Interruption.Begin"
    interruption_end = "Interruption.End"
    other = "Other"
    sample_clock = "Sample.Clock"
    sample_periodic = "Sample.Periodic"
    transaction_begin = "Transaction.Begin"
    transaction_end = "Transaction.End"
    trigger = "Trigger"

class ReasonType(StrEnum):
    de_authorized = "DeAuthorized"
    emergency_stop = "EmergencyStop"
    energy_limit_reached = "EnergyLimitReached"
    ev_disconnected = "EVDisconnected"
    ground_fault = "GroundFault"
    immediate_reset = "ImmediateReset"
    local = "Local"
    local_out_of_credit = "LocalOutOfCredit"
    master_pass = "MasterPass"
    other = "Other"
    overcurrent_fault = "OvercurrentFault"
    power_loss = "PowerLoss"
    power_quality = "PowerQuality"
    reboot = "Reboot"
    remote = "Remote"
    soc_limit_reached = "SOCLimitReached"
    stopped_by_ev = "StoppedByEV"
    time_limit_reached = "TimeLimitReached"
    timeout = "Timeout"

class RecurrencyKindType(StrEnum):
    daily = "Daily"
    weekly = "Weekly"

class RegistrationStatusType(StrEnum):
    accepted = "Accepted"
    pending = "Pending"
    rejected = "Rejected"

class ReportBaseType(StrEnum):
    configuration_inventory = "ConfigurationInventory"
    full_inventory = "FullInventory"
    summary_inventory = "SummaryInventory"

class RequestStartStopStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"

class ReservationUpdateStatusType(StrEnum):
    expired = "Expired"
    removed = "Removed"

class ReserveNowStatusType(StrEnum):
    accepted = "Accepted"
    faulted = "Faulted"
    occupied = "Occupied"
    rejected = "Rejected"
    unavailable = "Unavailable"

class ResetStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    scheduled = "Scheduled"

class ResetType(StrEnum):
    immediate = "Immediate"
    on_idle = "OnIdle"

class SendLocalListStatusType(StrEnum):
    accepted = "Accepted"
    failed = "Failed"
    version_mismatch = "VersionMismatch"

class SetMonitoringStatusType(StrEnum):
    accepted = "Accepted"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    unsupported_monitor_type = "UnsupportedMonitorType"
    rejected = "Rejected"
    duplicate = "Duplicate"

class SetNetworkProfileStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    failed = "Failed"

class SetVariableStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    unknown_component = "UnknownComponent"
    unknown_variable = "UnknownVariable"
    not_supported_attribute_type = "NotSupportedAttributeType"
    reboot_required = "RebootRequired"

class TransactionEventType(StrEnum):
    ended = "Ended"
    started = "Started"
    updated = "Updated"

class TriggerMessageStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    not_implemented = "NotImplemented"

class TriggerReasonType(StrEnum):
    authorized = "Authorized"
    cable_plugged_in = "CablePluggedIn"
    charging_rate_changed = "ChargingRateChanged"
    charging_state_changed = "ChargingStateChanged"
    deauthorized = "Deauthorized"
    energy_limit_reached = "EnergyLimitReached"
    ev_communication_lost = "EVCommunicationLost"
    ev_connect_timeout = "EVConnectTimeout"
    meter_value_clock = "MeterValueClock"
    meter_value_periodic = "MeterValuePeriodic"
    time_limit_reached = "TimeLimitReached"
    trigger = "Trigger"
    unlock_command = "UnlockCommand"
    stop_authorized = "StopAuthorized"
    ev_departed = "EVDeparted"
    ev_detected = "EVDetected"
    remote_stop = "RemoteStop"
    remote_start = "RemoteStart"
    abnormal_condition = "AbnormalCondition"
    signed_data_received = "SignedDataReceived"
    reset_command = "ResetCommand"

class TxStartStopPointType(StrEnum):
    authorized = "Authorized"
    data_signed = "DataSigned"
    energy_transfer = "EnergyTransfer"
    ev_connected = "EVConnected"
    parking_bay_occupancy = "ParkingBayOccupancy"
    power_path_closed = "PowerPathClosed"

class UnlockStatusType(StrEnum):
    unlocked = "Unlocked"
    unlock_failed = "UnlockFailed"
    ongoing_authorized_transaction = "OngoingAuthorizedTransaction"
    unknown_connector = "UnknownConnector"

class UnpublishFirmwareStatusType(StrEnum):
    download_ongoing = "DownloadOngoing"
    no_firmware = "NoFirmware"
    unpublished = "Unpublished"

class UpdateFirmwareStatusType(StrEnum):
    accepted = "Accepted"
    rejected = "Rejected"
    accepted_canceled = "AcceptedCanceled"
    invalid_certificate = "InvalidCertificate"
    revoked_certificate = "RevokedCertificate"

class UpdateType(StrEnum):
    differential = "Differential"
    full = "Full"

class UploadLogStatusType(StrEnum):
    bad_message = "BadMessage"
    idle = "Idle"
    not_supported_operation = "NotSupportedOperation"
    permission_denied = "PermissionDenied"
    uploaded = "Uploaded"
    upload_failure = "UploadFailure"
    uploading = "Uploading"
    accepted_canceled = "AcceptedCanceled"

class VPNType(StrEnum):
    ikev2 = "IKEv2"
    ipsec = "IPSec"
    l2tp = "L2TP"
    pptp = "PPTP"

class UnitOfMeasureType(StrEnum):
    asu = "ASU"
    b = "Bytes"
    db = "dB"
    dbm = "dBm"
    deg = "Deg"
    hz = "Hz"
    lx = "lx"
    m = "m"
    ms2 = "ms2"
    n = "N"
    ohm = "Ohm"
    kpa = "kPa"
    percent = "Percent"
    rh = "RH"
    rpm = "RPM"
    s = "s"
    va = "VA"
    kva = "kVA"
    vah = "VAh"
    kvah = "kVAh"
    var = "var"
    kvar = "kvar"
    varh = "varh"
    kvarh = "kvarh"
    wh = "Wh"
    kwh = "kWh"
    w = "W"
    kw = "kW"
    a = "A"
    v = "V"
    celsius = "Celsius"
    fahrenheit = "Fahrenheit"
    k = "K"

class StatusInfoReasonType(StrEnum):
    cs_not_accepted = "CSNotAccepted"
    duplicate_profile = "DuplicateProfile"
    duplicate_request_id = "DuplicateRequestId"
    fixed_cable = "FixedCable"
    fw_update_in_progress = "FwUpdateInProgress"
    internal_error = "InternalError"
    invalid_certificate = "InvalidCertificate"
    invalid_csr = "InvalidCSR"
    invalid_id_token = "InvalidIdToken"
    invalid_message_sequence = "InvalidMessageSequence"
    invalid_profile = "InvalidProfile"
    invalid_schedule = "InvalidSchedule"
    invalid_stack_level = "InvalidStackLevel"
    invalid_url = "InvalidURL"
    invalid_value = "InvalidValue"
    missing_device_model_info = "MissingDeviceModelInfo"
    missing_param = "MissingParam"
    no_cable = "NoCable"
    no_error = "NoError"
    not_enabled = "NotEnabled"
    not_found = "NotFound"
    out_of_memory = "OutOfMemory"
    out_of_storage = "OutOfStorage"
    read_only = "ReadOnly"
    too_large_element = "TooLargeElement"
    too_many_elements = "TooManyElements"
    tx_in_progress = "TxInProgress"
    tx_not_found = "TxNotFound"
    tx_started = "TxStarted"
    unknown_connector_id = "UnknownConnectorId"
    unknown_connector_type = "UnknownConnectorType"
    unknown_evse = "UnknownEvse"
    unknown_tx_id = "UnknownTxId"
    unspecified = "Unspecified"
    unsupported_param = "UnsupportedParam"
    unsupported_rate_unit = "UnsupportedRateUnit"
    unsupported_request = "UnsupportedRequest"
    value_out_of_range = "ValueOutOfRange"
    value_positive_only = "ValuePositiveOnly"
    value_too_high = "ValueTooHigh"
    value_too_low = "ValueTooLow"
    value_zero_not_allowed = "ValueZeroNotAllowed"
    write_only = "WriteOnly"

class SecurityEventType(StrEnum):
    firmware_updated = "FirmwareUpdated"
    failed_to_authenticate_at_csms = "FailedToAuthenticateAtCsms"
    csms_failed_to_authenticate = "CsmsFailedToAuthenticate"
    setting_system_time = "SettingSystemTime"
    startup_of_the_device = "StartupOfTheDevice"
    reset_or_reboot = "ResetOrReboot"
    security_log_was_cleared = "SecurityLogWasCleared"
    reconfiguration_of_security_parameters = "ReconfigurationOfSecurityParameters"
    memory_exhaustion = "MemoryExhaustion"
    invalid_messages = "InvalidMessages"
    attempted_replay_attacks = "AttemptedReplayAttacks"
    tamper_detection_activated = "TamperDetectionActivated"
    invalid_firmware_signature = "InvalidFirmwareSignature"
    invalid_firmware_signing_certificate = "InvalidFirmwareSigningCertificate"
    invalid_csms_certificate = "InvalidCsmsCertificate"
    invalid_charging_station_certificate = "InvalidChargingStationCertificate"
    invalid_tls_version = "InvalidTLSVersion"
    invalid_tls_cipher_suite = "InvalidTLSCipherSuite"
    maintenance_login_accepted = "MaintenanceLoginAccepted"
    maintenance_login_failed = "MaintenanceLoginFailed"

class ControllerComponentName(StrEnum):
    aligned_data_ctrlr = "AlignedDataCtrlr"
    auth_cache_ctrlr = "AuthCacheCtrlr"
    auth_ctrlr = "AuthCtrlr"
    chademo_ctrlr = "CHAdeMOCtrlr"
    clock_ctrlr = "ClockCtrlr"
    customization_ctrlr = "CustomizationCtrlr"
    device_data_ctrlr = "DeviceDataCtrlr"
    display_message_ctrlr = "DisplayMessageCtrlr"
    iso15118_ctrlr = "ISO15118Ctrlr"
    local_auth_list_ctrlr = "LocalAuthListCtrlr"
    monitoring_ctrlr = "MonitoringCtrlr"
    ocpp_comm_ctrlr = "OCPPCommCtrlr"
    reservation_ctrlr = "ReservationCtrlr"
    sampled_data_ctrlr = "SampledDataCtrlr"
    security_ctrlr = "SecurityCtrlr"
    smart_charging_ctrlr = "SmartChargingCtrlr"
    tariff_cost_ctrlr = "TariffCostCtrlr"
    tx_ctrlr = "TxCtrlr"

class PhysicalComponentName(StrEnum):
    access_barrier = "AccessBarrier"
    ac_dc_converter = "AcDcConverter"
    ac_phase_selector = "AcPhaseSelector"
    actuator = "Actuator"
    air_cooling_system = "AirCoolingSystem"
    area_ventilation = "AreaVentilation"
    bay_occupancy_sensor = "BayOccupancySensor"
    beacon_lighting = "BeaconLighting"
    cable_breakaway_sensor = "CableBreakawaySensor"
    case_access_sensor = "CaseAccessSensor"
    charging_station = "ChargingStation"
    charging_status_indicator = "ChargingStatusIndicator"
    connected_ev = "ConnectedEV"
    connector = "Connector"
    connector_holster_release = "ConnectorHolsterRelease"
    connector_holster_sensor = "ConnectorHolsterSensor"
    connector_plug_retention_lock = "ConnectorPlugRetentionLock"
    connector_protection_release = "ConnectorProtectionRelease"
    controller = "Controller"
    control_metering = "ControlMetering"
    cppwm_controller = "CPPWMController"
    data_link = "DataLink"
    display = "Display"
    distribution_panel = "DistributionPanel"
    electrical_feed = "ElectricalFeed"
    elv_supply = "ELVSupply"
    emergency_stop_sensor = "EmergencyStopSensor"
    environmental_lighting = "EnvironmentalLighting"
    ev_retention_lock = "EVRetentionLock"
    evse = "EVSE"
    external_temperature_sensor = "ExternalTemperatureSensor"
    fiscal_metering = "FiscalMetering"
    flood_sensor = "FloodSensor"
    ground_isolation_protection = "GroundIsolationProtection"
    heater = "Heater"
    humidity_sensor = "HumiditySensor"
    light_sensor = "LightSensor"
    liquid_cooling_system = "LiquidCoolingSystem"
    local_availability_sensor = "LocalAvailabilitySensor"
    local_controller = "LocalController"
    local_energy_storage = "LocalEnergyStorage"
    over_current_protection = "OverCurrentProtection"
    over_current_protection_recloser = "OverCurrentProtectionRecloser"
    power_contactor = "PowerContactor"
    rcd = "RCD"
    rcd_recloser = "RCDRecloser"
    real_time_clock = "RealTimeClock"
    shock_sensor = "ShockSensor"
    spaces_count_signage = "SpacesCountSignage"
    switch = "Switch"
    temperature_sensor = "TemperatureSensor"
    tilt_sensor = "TiltSensor"
    token_reader = "TokenReader"
    ui_input = "UIInput"
    upstream_protection_trigger = "UpstreamProtectionTrigger"
    vehicle_id_sensor = "VehicleIdSensor"

class GenericVariableName(StrEnum):
    ac_current = "ACCurrent"
    active = "Active"
    ac_voltage = "ACVoltage"
    allow_reset = "AllowReset"
    angle = "Angle"
    attempts = "Attempts"
    availability_state = "AvailabilityState"
    available = "Available"
    certificate = "Certificate"
    charge_protocol = "ChargeProtocol"
    charging_complete_bulk = "ChargingCompleteBulk"
    charging_complete_full = "ChargingCompleteFull"
    charging_time = "ChargingTime"
    color = "Color"
    complete = "Complete"
    connected_time = "ConnectedTime"
    connector_type = "ConnectorType"
    count = "Count"  # type: ignore[assignment]
    currency = "Currency"
    current_imbalance = "CurrentImbalance"
    data_text = "DataText"
    date_time = "DateTime"
    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"
    departure_time = "DepartureTime"
    ec_variant = "ECVariant"
    enabled = "Enabled"
    energy = "Energy"
    energy_capacity = "EnergyCapacity"
    energy_export = "EnergyExport"
    energy_export_register = "EnergyExportRegister"
    energy_import = "EnergyImport"
    energy_import_register = "EnergyImportRegister"
    entries = "Entries"
    evse_id = "EvseId"
    fallback = "Fallback"
    fan_speed = "FanSpeed"
    firmware_version = "FirmwareVersion"
    force = "Force"
    formats = "Formats"
    frequency = "Frequency"
    fuse_rating = "FuseRating"
    height = "Height"
    humidity = "Humidity"
    hysteresis = "Hysteresis"
    iccid = "ICCID"
    impedance = "Impedance"
    imsi = "IMSI"
    interval = "Interval"
    length = "Length"
    light = "Light"
    manufacturer = "Manufacturer"
    message = "Message"
    minimum_status_duration = "MinimumStatusDuration"
    mode = "Mode"
    model = "Model"
    network_address = "NetworkAddress"
    operated = "Operated"
    operating_times = "OperatingTimes"
    overload = "Overload"
    percent = "Percent"
    phase_rotation = "PhaseRotation"
    post_charging_time = "PostChargingTime"
    power = "Power"
    problem = "Problem"
    protecting = "Protecting"
    remaining_time_bulk = "RemainingTimeBulk"
    remaining_time_full = "RemainingTimeFull"
    secc_id = "SeccId"
    serial_number = "SerialNumber"
    signal_strength = "SignalStrength"
    state = "State"
    state_of_charge = "StateOfCharge"
    state_of_charge_bulk = "StateOfChargeBulk"
    storage = "Storage"
    supply_phases = "SupplyPhases"
    suspending = "Suspending"
    suspension = "Suspension"
    temperature = "Temperature"
    time = "Time"
    time_offset = "TimeOffset"
    timeout = "Timeout"
    token = "Token"
    token_type = "TokenType"
    tries = "Tries"
    tripped = "Tripped"
    vehicle_id = "VehicleId"
    version_date = "VersionDate"
    version_number = "VersionNumber"
    voltage_imbalance = "VoltageImbalance"

class AlignedDataCtrlrVariableName(StrEnum):
    available = "Available"
    enabled = "Enabled"
    interval = "Interval"
    measurands = "Measurands"
    send_during_idle = "SendDuringIdle"
    sign_readings = "SignReadings"
    tx_ended_interval = "TxEndedInterval"
    tx_ended_measurands = "TxEndedMeasurands"

class AuthCacheCtrlrVariableName(StrEnum):
    available = "Available"
    enabled = "Enabled"
    life_time = "LifeTime"
    policy = "Policy"
    storage = "Storage"
    disable_post_authorize = "DisablePostAuthorize"

class AuthCtrlrVariableName(StrEnum):
    additional_info_items_per_message = "AdditionalInfoItemsPerMessage"
    authorize_remote_start = "AuthorizeRemoteStart"
    enabled = "Enabled"
    local_authorize_offline = "LocalAuthorizeOffline"
    local_pre_authorize = "LocalPreAuthorize"
    master_pass_group_id = "MasterPassGroupId"
    offline_tx_for_unknown_id_enabled = "OfflineTxForUnknownIdEnabled"
    disable_remote_authorization = "DisableRemoteAuthorization"

class CHAdeMOCtrlrVariableName(StrEnum):
    enabled = "Enabled"
    active = "Active"
    complete = "Complete"
    tripped = "Tripped"
    problem = "Problem"
    selftest_active = "SelftestActive"
    selftest_active_set = "SelftestActive(Set)"
    chademo_protocol_number = "CHAdeMOProtocolNumber"
    vehicle_status = "VehicleStatus"
    dynamic_control = "DynamicControl"
    high_current_control = "HighCurrentControl"
    high_voltage_control = "HighVoltageControl"
    auto_manufacturer_code = "AutoManufacturerCode"

class ClockCtrlrVariableName(StrEnum):
    date_time = "DateTime"
    next_time_offset_transition_date_time = "NextTimeOffsetTransitionDateTime"
    ntp_server_uri = "NtpServerUri"
    ntp_source = "NtpSource"
    time_adjustment_reporting_threshold = "TimeAdjustmentReportingThreshold"
    time_offset = "TimeOffset"
    time_source = "TimeSource"
    time_zone = "TimeZone"

class CustomizationCtrlrVariableName(StrEnum):
    custom_implementation_enabled = "CustomImplementationEnabled"

class DeviceDataCtrlrVariableName(StrEnum):
    bytes_per_message = "BytesPerMessage"
    configuration_value_size = "ConfigurationValueSize"
    items_per_message = "ItemsPerMessage"
    reporting_value_size = "ReportingValueSize"
    value_size = "ValueSize"

class DeviceDataCtrlrInstanceName(StrEnum):
    get_report = "GetReport"
    get_variables = "GetVariables"
    set_variables = "SetVariables"

class DisplayMessageCtrlrVariableName(StrEnum):
    available = "Available"
    display_messages = "DisplayMessages"
    enabled = "Enabled"
    personal_message_size = "PersonalMessageSize"
    supported_formats = "SupportedFormats"
    supported_priorities = "SupportedPriorities"

class ISO15118CtrlrVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    central_contract_validation_allowed = "CentralContractValidationAllowed"
    complete = "Complete"
    contract_validation_offline = "ContractValidationOffline"
    secc_id = "SeccId"
    selftest_active = "SelftestActive"
    selftest_active_set = "SelftestActive(Set)"
    max_schedule_entries = "MaxScheduleEntries"
    requested_energy_transfer_mode = "RequestedEnergyTransferMode"
    request_metering_receipt = "RequestMeteringReceipt"
    country_name = "CountryName"
    organization_name = "OrganizationName"
    pnc_enabled = "PnCEnabled"
    problem = "Problem"
    tripped = "Tripped"
    v2g_certificate_installation_enabled = "V2GCertificateInstallationEnabled"
    contract_certificate_installation_enabled = "ContractCertificateInstallationEnabled"

class LocalAuthListCtrlrVariableName(StrEnum):
    available = "Available"
    bytes_per_message = "BytesPerMessage"
    enabled = "Enabled"
    entries = "Entries"
    items_per_message = "ItemsPerMessage"
    storage = "Storage"
    disable_post_authorize = "DisablePostAuthorize"

class MonitoringCtrlrVariableName(StrEnum):
    available = "Available"
    bytes_per_message = "BytesPerMessage"
    enabled = "Enabled"
    items_per_message = "ItemsPerMessage"
    offline_queuing_severity = "OfflineQueuingSeverity"
    monitoring_base = "MonitoringBase"
    monitoring_level = "MonitoringLevel"
    active_monitoring_base = "ActiveMonitoringBase"
    active_monitoring_level = "ActiveMonitoringLevel"

class MonitoringCtrlrInstanceName(StrEnum):
    clear_variable_monitoring = "ClearVariableMonitoring"
    set_variable_monitoring = "SetVariableMonitoring"

class OCPPCommCtrlrVariableName(StrEnum):
    active_network_profile = "ActiveNetworkProfile"
    file_transfer_protocols = "FileTransferProtocols"
    heartbeat_interval = "HeartbeatInterval"
    message_timeout = "MessageTimeout"
    message_attempt_interval = "MessageAttemptInterval"
    message_attempts = "MessageAttempts"
    minimum_status_duration = "MinimumStatusDuration"
    network_configuration_priority = "NetworkConfigurationPriority"
    network_profile_connection_attempts = "NetworkProfileConnectionAttempts"
    offline_threshold = "OfflineThreshold"
    public_key_with_signed_meter_value = "PublicKeyWithSignedMeterValue"
    queue_all_messages = "QueueAllMessages"
    reset_retries = "ResetRetries"
    retry_back_off_random_range = "RetryBackOffRandomRange"
    retry_back_off_repeat_times = "RetryBackOffRepeatTimes"
    retry_back_off_wait_minimum = "RetryBackOffWaitMinimum"
    unlock_on_ev_side_disconnect = "UnlockOnEVSideDisconnect"
    web_socket_ping_interval = "WebSocketPingInterval"
    field_length = "FieldLength"

class OCPPCommCtrlrInstanceName(StrEnum):
    default = "Default"
    transaction_event = "TransactionEvent"

class ReservationCtrlrVariableName(StrEnum):
    available = "Available"
    enabled = "Enabled"
    non_evse_specific = "NonEvseSpecific"

class SampledDataCtrlrVariableName(StrEnum):
    available = "Available"
    enabled = "Enabled"
    sign_readings = "SignReadings"
    tx_ended_interval = "TxEndedInterval"
    tx_ended_measurands = "TxEndedMeasurands"
    tx_started_measurands = "TxStartedMeasurands"
    tx_updated_interval = "TxUpdatedInterval"
    tx_updated_measurands = "TxUpdatedMeasurands"
    register_values_without_phases = "RegisterValuesWithoutPhases"

class SecurityCtrlrVariableName(StrEnum):
    additional_root_certificate_check = "AdditionalRootCertificateCheck"
    basic_auth_password = "BasicAuthPassword"
    certificate_entries = "CertificateEntries"
    cert_signing_repeat_times = "CertSigningRepeatTimes"
    cert_signing_wait_minimum = "CertSigningWaitMinimum"
    identity = "Identity"
    max_certificate_chain_size = "MaxCertificateChainSize"
    organization_name = "OrganizationName"
    security_profile = "SecurityProfile"

class SmartChargingCtrlrVariableName(StrEnum):
    ac_phase_switching_supported = "ACPhaseSwitchingSupported"
    available = "Available"
    enabled = "Enabled"
    entries = "Entries"
    external_control_signals_enabled = "ExternalControlSignalsEnabled"
    limit_change_significance = "LimitChangeSignificance"
    notify_charging_limit_with_schedules = "NotifyChargingLimitWithSchedules"
    periods_per_schedule = "PeriodsPerSchedule"
    phases_3to1 = "Phases3to1"
    profile_stack_level = "ProfileStackLevel"
    rate_unit = "RateUnit"

class SmartChargingCtrlrInstanceName(StrEnum):
    charging_profiles = "ChargingProfiles"

class TariffCostCtrlrVariableName(StrEnum):
    available = "Available"
    currency = "Currency"
    enabled = "Enabled"
    tariff_fallback_message = "TariffFallbackMessage"
    total_cost_fallback_message = "TotalCostFallbackMessage"

class TariffCostCtrlrInstanceName(StrEnum):
    tariff = "Tariff"
    cost = "Cost"

class TxCtrlrVariableName(StrEnum):
    charging_time = "ChargingTime"
    ev_connection_time_out = "EVConnectionTimeOut"
    max_energy_on_invalid_id = "MaxEnergyOnInvalidId"
    stop_tx_on_ev_side_disconnect = "StopTxOnEVSideDisconnect"
    stop_tx_on_invalid_id = "StopTxOnInvalidId"
    tx_before_accepted_enabled = "TxBeforeAcceptedEnabled"
    tx_start_point = "TxStartPoint"
    tx_stop_point = "TxStopPoint"

class AccessBarrierVariableName(StrEnum):
    enabled = "Enabled"
    active = "Active"
    problem = "Problem"

class AcDcConverterVariableName(StrEnum):
    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"
    enabled = "Enabled"
    fan_speed = "FanSpeed"
    overload = "Overload"
    power = "Power"
    problem = "Problem"
    temperature = "Temperature"
    tripped = "Tripped"

class AcPhaseSelectorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    phase_rotation = "PhaseRotation"
    problem = "Problem"

class ActuatorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    state = "State"

class AirCoolingSystemVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    fan_speed = "FanSpeed"

class AreaVentilationVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    fan_speed = "FanSpeed"

class BayOccupancySensorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    percent = "Percent"

class BeaconLightingVariableName(StrEnum):
    active = "Active"
    color = "Color"
    enabled = "Enabled"
    enabled_set = "Enabled(Set)"
    percent = "Percent"
    percent_set = "Percent(Set)"
    power = "Power"
    problem = "Problem"

class CableBreakawaySensorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    tripped = "Tripped"

class CaseAccessSensorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    enabled_set = "Enabled(Set)"
    problem = "Problem"
    tripped = "Tripped"

class ChargingStationVariableName(StrEnum):
    ac_current = "ACCurrent"
    ac_voltage = "ACVoltage"
    ac_voltage_max_limit = "ACVoltage(MaxLimit)"
    allow_new_sessions_pending_firmware_update = "AllowNewSessionsPendingFirmwareUpdate"
    available = "Available"
    availability_state = "AvailabilityState"
    charge_protocol = "ChargeProtocol"
    current_imbalance = "CurrentImbalance"
    ec_variant = "ECVariant"
    enabled = "Enabled"
    identity = "Identity"
    model = "Model"
    operating_times = "OperatingTimes"
    overload = "Overload"
    phase_rotation = "PhaseRotation"
    power = "Power"
    power_max_limit = "Power(MaxLimit)"
    problem = "Problem"
    serial_number = "SerialNumber"
    supply_phases = "SupplyPhases"
    supply_phases_max_limit = "SupplyPhases(MaxLimit)"
    tripped = "Tripped"
    vendor_name = "VendorName"
    voltage_imbalance = "VoltageImbalance"

class ChargingStatusIndicatorVariableName(StrEnum):
    active = "Active"
    color = "Color"

class ConnectedEVVariableName(StrEnum):
    protocol_agreed = "ProtocolAgreed"
    protocol_supported_by_ev = "ProtocolSupportedByEV"
    vehicle_id = "VehicleId"
    ac_current = "ACCurrent"
    ac_voltage = "ACVoltage"
    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"
    power = "Power"
    energy_import = "EnergyImport"
    departure_time = "DepartureTime"
    energy_capacity = "EnergyCapacity"
    remaining_time_bulk = "RemainingTimeBulk"
    remaining_time_full = "RemainingTimeFull"
    state_of_charge = "StateOfCharge"
    state_of_charge_bulk = "StateOfChargeBulk"
    charging_complete_bulk = "ChargingCompleteBulk"
    charging_complete_full = "ChargingCompleteFull"

class ChargingStateVariableName(StrEnum):
    battery_overvoltage = "BatteryOvervoltage"
    battery_undervoltage = "BatteryUndervoltage"
    charging_current_deviation = "ChargingCurrentDeviation"
    battery_temperature = "BatteryTemperature"
    voltage_deviation = "VoltageDeviation"
    charging_system_error = "ChargingSystemError"
    vehicle_shift_position = "VehicleShiftPosition"
    vehicle_charging_enabled = "VehicleChargingEnabled"
    charging_system_incompatibility = "ChargingSystemIncompatibility"
    charger_connector_lock_fault = "ChargerConnectorLockFault"

class ConnectorVariableName(StrEnum):
    availability_state = "AvailabilityState"
    available = "Available"
    charge_protocol = "ChargeProtocol"
    connector_type = "ConnectorType"
    enabled = "Enabled"
    phase_rotation = "PhaseRotation"
    problem = "Problem"
    supply_phases = "SupplyPhases"
    supply_phases_max_limit = "SupplyPhases(MaxLimit)"
    tripped = "Tripped"

class ConnectorHolsterReleaseVariableName(StrEnum):
    enabled = "Enabled"
    active = "Active"
    problem = "Problem"
    state = "State"

class ConnectorHolsterSensorVariableName(StrEnum):
    enabled = "Enabled"
    active = "Active"
    problem = "Problem"

class ConnectorPlugRetentionLockVariableName(StrEnum):
    enabled = "Enabled"
    active = "Active"
    problem = "Problem"
    tripped = "Tripped"
    tries = "Tries"
    tries_set_limit = "Tries(SetLimit)"
    tries_max_limit = "Tries(MaxLimit)"

class ConnectorProtectionReleaseVariableName(StrEnum):
    enabled = "Enabled"
    active = "Active"
    problem = "Problem"
    tripped = "Tripped"

class ControllerVariableName(StrEnum):
    active = "Active"
    ec_variant = "ECVariant"
    firmware_version = "FirmwareVersion"
    interval_heartbeat = "Interval[Heartbeat]"
    manufacturer = "Manufacturer"
    max_msg_elements = "MaxMsgElements"
    model = "Model"
    problem = "Problem"
    selftest_active = "SelftestActive"
    selftest_active_set = "SelftestActive(Set)"
    serial_number = "SerialNumber"
    version_date = "VersionDate"
    version_number = "VersionNumber"

class ControlMeteringVariableName(StrEnum):
    power = "Power"
    ac_current = "ACCurrent"
    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"

class CPPWMControllerVariableName(StrEnum):
    active = "Active"
    dc_voltage = "DCVoltage"
    enabled = "Enabled"
    percentage = "Percentage"
    problem = "Problem"
    selftest_active = "SelftestActive"
    selftest_active_set = "SelftestActive(Set)"
    state = "State"

class DataLinkVariableName(StrEnum):
    active = "Active"
    complete = "Complete"
    enabled = "Enabled"
    fallback = "Fallback"
    iccid = "ICCID"
    imsi = "IMSI"
    network_address = "NetworkAddress"
    problem = "Problem"
    signal_strength = "SignalStrength"

class DisplayVariableName(StrEnum):
    color = "Color"
    count_height_in_chars = "Count[HeightInChars]"
    count_width_in_chars = "Count[WidthInChars]"
    data_text_visible = "DataText[Visible]"
    enabled = "Enabled"
    problem = "Problem"
    state = "State"

class DistributionPanelVariableName(StrEnum):
    charging_station = "ChargingStation"
    distribution_panel = "DistributionPanel"
    fuse = "Fuse"
    instance_name = "InstanceName"

class ElectricalFeedVariableName(StrEnum):
    ac_voltage = "ACVoltage"
    active = "Active"
    dc_voltage = "DCVoltage"
    enabled = "Enabled"
    energy = "Energy"
    phase_rotation = "PhaseRotation"
    power = "Power"
    power_type = "PowerType"
    problem = "Problem"
    supply_phases = "SupplyPhases"

class ELVSupplyVariableName(StrEnum):
    energy_import_register = "EnergyImportRegister"
    fallback = "Fallback"
    fallback_max_limit = "Fallback(MaxLimit)"
    power = "Power"
    power_max_limit = "Power(MaxLimit)"
    state_of_charge = "StateOfCharge"
    time = "Time"

class EmergencyStopSensorVariableName(StrEnum):
    enabled = "Enabled"
    active = "Active"
    tripped = "Tripped"

class EnvironmentalLightingVariableName(StrEnum):
    active = "Active"
    color = "Color"
    enabled = "Enabled"
    enabled_set = "Enabled(Set)"
    percent = "Percent"
    percent_set = "Percent(Set)"
    power = "Power"
    problem = "Problem"

class EVRetentionLockVariableName(StrEnum):
    active = "Active"
    complete = "Complete"
    enabled = "Enabled"
    problem = "Problem"

class EVSEVariableName(StrEnum):
    ac_current = "ACCurrent"
    ac_voltage = "ACVoltage"
    available = "Available"
    availability_state = "AvailabilityState"
    allow_reset = "AllowReset"
    charge_protocol = "ChargeProtocol"
    charging_time = "ChargingTime"
    count_charging_profiles_max_limit = "Count[ChargingProfiles](MaxLimit)"
    count_charging_profiles = "Count[ChargingProfiles]"
    current_imbalance = "CurrentImbalance"
    dc_current = "DCCurrent"
    dc_voltage = "DCVoltage"
    enabled = "Enabled"
    evse_id = "EvseId"
    iso15118_evse_id = "ISO15118EvseId"
    overload = "Overload"
    phase_rotation = "PhaseRotation"
    post_charging_time = "PostChargingTime"
    power = "Power"
    problem = "Problem"
    supply_phases = "SupplyPhases"
    tripped = "Tripped"
    voltage_imbalance = "VoltageImbalance"

class ExternalTemperatureSensorVariableName(StrEnum):
    active = "Active"
    problem = "Problem"
    temperature = "Temperature"

class FiscalMeteringVariableName(StrEnum):
    problem = "Problem"
    certificate = "Certificate"
    ec_variant = "ECVariant"
    energy_export = "EnergyExport"
    energy_export_register = "EnergyExportRegister"
    energy_import = "EnergyImport"
    energy_import_register = "EnergyImportRegister"
    manufacturer_ct = "Manufacturer[CT]"
    manufacturer_meter = "Manufacturer[Meter]"
    model_ct = "Model[CT]"
    model_meter = "Model[Meter]"
    options_set_meter_value_aligned_data = "OptionsSet[MeterValueAlignedData]"
    options_set_txn_stopped_aligned_data = "OptionsSet[TxnStoppedAlignedData]"
    serial_number_ct = "SerialNumber[CT]"
    serial_number_meter = "SerialNumber[Meter]"

class FloodSensorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    height = "Height"
    percent = "Percent"
    tripped = "Tripped"

class GroundIsolationProtectionVariableName(StrEnum):
    active = "Active"
    complete = "Complete"
    enabled = "Enabled"
    impedance = "Impedance"
    problem = "Problem"

class HeaterVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    tripped = "Tripped"
    power = "Power"
    power_max_limit = "Power(MaxLimit)"
    power_max_set = "Power(MaxSet)"
    temperature_min_set = "Temperature(MinSet)"
    temperature_max_set = "Temperature(MaxSet)"

class HumiditySensorVariableName(StrEnum):
    enabled = "Enabled"
    humidity = "Humidity"
    problem = "Problem"

class LightSensorVariableName(StrEnum):
    enabled = "Enabled"
    light = "Light"
    problem = "Problem"

class LiquidCoolingSystemVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    problem = "Problem"
    temperature = "Temperature"

class LocalAvailabilitySensorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    problem = "Problem"

class LocalControllerVariableName(StrEnum):
    charging_station = "ChargingStation"
    distribution_panel = "DistributionPanel"
    ec_variant = "ECVariant"
    enabled = "Enabled"
    identity = "Identity"
    manufacturer = "Manufacturer"
    model = "Model"
    problem = "Problem"
    serial_number = "SerialNumber"
    tripped = "Tripped"

class LocalEnergyStorageVariableName(StrEnum):
    capacity = "Capacity"
    energy_capacity = "EnergyCapacity"
    identity = "Identity"

class OverCurrentProtectionVariableName(StrEnum):
    ac_current = "ACCurrent"
    active = "Active"
    operated = "Operated"

class OverCurrentProtectionRecloserVariableName(StrEnum):
    active = "Active"
    active_set = "Active(Set)"
    enabled = "Enabled"
    complete = "Complete"
    problem = "Problem"
    mode = "Mode"
    tries = "Tries"
    tries_set_limit = "Tries(SetLimit)"
    tries_max_limit = "Tries(MaxLimit)"

class PowerContactorVariableName(StrEnum):
    active = "Active"
    problem = "Problem"
    tripped = "Tripped"

class RCDVariableName(StrEnum):
    operated = "Operated"
    tripped = "Tripped"

class RCDRecloserVariableName(StrEnum):
    active = "Active"
    active_set = "Active(Set)"
    complete = "Complete"
    enabled = "Enabled"
    problem = "Problem"
    tries = "Tries"
    tries_max_limit = "Tries(MaxLimit)"
    tries_set_limit = "Tries(SetLimit)"

class RealTimeClockVariableName(StrEnum):
    active = "Active"
    dc_voltage = "DCVoltage"
    fallback = "Fallback"
    fallback_max_limit = "Fallback(MaxLimit)"
    problem = "Problem"

class ShockSensorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    force = "Force"

class SpacesCountSignageVariableName(StrEnum):
    active = "Active"
    count = "Count"  # type: ignore[assignment]
    enabled = "Enabled"

class SwitchVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    state = "State"

class TemperatureSensorVariableName(StrEnum):
    active = "Active"
    problem = "Problem"
    temperature = "Temperature"

class TiltSensorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    angle = "Angle"

class TokenReaderVariableName(StrEnum):
    enabled = "Enabled"
    enabled_set = "Enabled(Set)"
    operated = "Operated"
    problem = "Problem"
    token = "Token"
    token_type = "TokenType"

class UIInputVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
    operated = "Operated"

class UpstreamProtectionTriggerVariableName(StrEnum):
    active_set = "Active(Set)"
    enabled = "Enabled"
    problem = "Problem"
    tripped = "Tripped"

class VehicleIdSensorVariableName(StrEnum):
    active = "Active"
    enabled = "Enabled"
