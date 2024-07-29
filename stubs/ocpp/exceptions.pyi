from _typeshed import Incomplete

class OCPPError(Exception):
    default_description: str
    description: Incomplete
    details: Incomplete
    def __init__(self, description: Incomplete | None = None, details: Incomplete | None = None) -> None: ...
    def __eq__(self, other): ...

class NotImplementedError(OCPPError):
    code: str
    default_description: str

class NotSupportedError(OCPPError):
    code: str
    default_description: str

class InternalError(OCPPError):
    code: str
    default_description: str

class ProtocolError(OCPPError):
    code: str
    default_description: str

class SecurityError(OCPPError):
    code: str
    default_description: str

class FormatViolationError(OCPPError):
    code: str
    default_description: str

class FormationViolationError(OCPPError):
    code: str
    default_description: str

class PropertyConstraintViolationError(OCPPError):
    code: str
    default_description: str

class OccurenceConstraintViolationError(OCPPError):
    code: str
    default_description: str

class OccurrenceConstraintViolationError(OCPPError):
    code: str
    default_description: str

class TypeConstraintViolationError(OCPPError):
    code: str
    default_description: str

class GenericError(OCPPError):
    code: str
    default_description: str

class ValidationError(Exception): ...
class UnknownCallErrorCodeError(Exception): ...
