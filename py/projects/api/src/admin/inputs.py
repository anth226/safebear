from enum import StrEnum, auto
from typing import Optional

import strawberry
from strawberry.utils.str_converters import to_camel_case

from ..app._types import Plan, User


@strawberry.input
class UserFiltersInput:
    query: Optional[str] = strawberry.UNSET
    plan: Optional[Plan] = strawberry.UNSET


@strawberry.enum
class DirectionEnum(StrEnum):
    ASC = auto()
    DESC = auto()


UserField = strawberry.enum(
    name="UserField",
    description="User field names",
    _cls=StrEnum(
        "UserField", {to_camel_case(field): field for field in User.__fields__.keys()}
    ),
)


@strawberry.input
class UserOrderByInput:
    field: UserField  # pyright: ignore
    direction: DirectionEnum = DirectionEnum.ASC


@strawberry.input
class UpdateUserInput:
    first_name: Optional[str] = strawberry.UNSET
    last_name: Optional[str] = strawberry.UNSET
    email: Optional[str] = strawberry.UNSET
