from _typeshed import Incomplete

routables: Incomplete

from typing import Callable, ParamSpec, Concatenate, TypeVar, Any

Param = ParamSpec("Param")
RetType = TypeVar("RetType")
TFunc = Callable[Param, RetType]

def on(action: Any, *, skip_schema_validation: bool = False) -> Callable[[TFunc], TFunc]: ...
def after(action: Any) -> Callable[[TFunc], TFunc]: ...
def create_route_map(obj): ...
