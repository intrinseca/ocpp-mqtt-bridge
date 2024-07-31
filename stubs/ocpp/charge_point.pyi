from _typeshed import Incomplete
from ocpp.exceptions import NotImplementedError as NotImplementedError, NotSupportedError as NotSupportedError, OCPPError as OCPPError
from ocpp.messages import Call as Call, MessageType as MessageType, unpack as unpack, validate_payload as validate_payload
from ocpp.routing import create_route_map as create_route_map

LOGGER: Incomplete

def camel_to_snake_case(data): ...
def snake_to_camel_case(data): ...
def serialize_as_dict(dataclass): ...
def remove_nones(data: list | dict) -> list | dict: ...

class ChargePoint:
    id: Incomplete
    route_map: Incomplete
    def __init__(self, id, connection, response_timeout: int = 30) -> None: ...
    async def start(self) -> None: ...
    async def route_message(self, raw_msg) -> None: ...
    async def call(self, payload, suppress: bool = True, unique_id: Incomplete | None = None): ...