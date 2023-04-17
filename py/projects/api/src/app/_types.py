from datetime import datetime
from enum import StrEnum, auto

import strawberry

from .._types import Label
from .models import (
    DocumentTypeEnum,
    LinkedAccount,
    Message,
    PlanEnum,
    PlatformEnum,
    User,
    UserActionHistory,
)

# Enums

Platform = strawberry.enum(
    _cls=PlatformEnum,
    name="Platform",
    description="Social media platform",
)

DocumentType = strawberry.enum(
    _cls=DocumentTypeEnum,
    name="DocumentType",
    description="Type of identity document",
)

Plan = strawberry.enum(
    _cls=PlanEnum,
    name="Plan",
    description="Subscription plan",
)

# Models


@strawberry.experimental.pydantic.type(
    model=LinkedAccount,
    name=LinkedAccount.__name__,
    description="A user's social media account",
)
class LinkedAccountType:
    platform: strawberry.auto
    logo_url: strawberry.auto


@strawberry.type(description="Statistics for a given timeframe")
class StatisticsType:
    total_messages: int
    toxic_messages: int
    blocked_messages: int


@strawberry.type(description="User statistics")
class UserStatisticsType:
    day: StatisticsType
    week: StatisticsType
    month: StatisticsType
    two_months: StatisticsType
    quarter: StatisticsType


@strawberry.experimental.pydantic.type(
    model=User, name="Child", description="A User's child"
)
class ChildType:
    first_name: strawberry.auto
    avatar_url: strawberry.auto
    linked_accounts: strawberry.auto
    stats: UserStatisticsType


@strawberry.experimental.pydantic.type(
    model=User, name=User.__name__, description="A user account"
)
class UserType:
    id: strawberry.auto
    email: strawberry.auto
    first_name: strawberry.auto
    last_name: strawberry.auto
    full_name: strawberry.auto
    avatar_url: strawberry.auto
    birthday: strawberry.auto
    linked_accounts: strawberry.auto
    onboarding_completed: strawberry.auto
    plan: strawberry.auto
    identity_verified: strawberry.auto
    age: strawberry.auto
    is_minor: strawberry.auto
    is_parent: strawberry.auto
    created_at: strawberry.auto
    stats: UserStatisticsType
    # children: list[ChildType]


@strawberry.type(description="Pharos summarized data")
class PharosReportType:
    first_name: str
    last_name: str
    gender: str
    age: int
    city: str
    country: str
    email: str
    platform_url: str
    body: str


@strawberry.experimental.pydantic.type(
    model=Message, all_fields=True, name=Message.__name__
)
class MessageType:
    pass


@strawberry.type(description="A toxic user")
class BullyType:
    handle: strawberry.ID
    platform: Platform
    num_toxic_messages: int
    labels: list[Label]
    last_message: datetime


@strawberry.enum(name="BullyOrderBy")
class BullyOrderByEnum(StrEnum):
    DATE = auto()
    FREQUENCY = auto()
    VIRULENCE = auto()


@strawberry.experimental.pydantic.type(
    model=UserActionHistory,
    name=UserActionHistory.__name__,
    description="An action taken by a user",
)
class UserActionHistoryType:
    timestamp: strawberry.auto
    title: strawberry.auto
    body: strawberry.auto
