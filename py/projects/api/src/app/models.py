from datetime import date, datetime
from enum import StrEnum, auto

from pydantic import UUID4, BaseModel, Field, HttpUrl, validator

from ..base_models import BaseLabelingModel, BaseUser


class PlanEnum(StrEnum):
    BASIC = auto()
    SAFE = auto()


class Plan(BaseModel):
    id: UUID4
    name: PlanEnum
    price: float


class PlatformEnum(StrEnum):
    FACEBOOK = auto()
    INSTAGRAM = auto()
    TWITTER = auto()


class LinkedAccount(BaseModel):
    """
    A user's social media account
    """

    platform: PlatformEnum
    logo_url: HttpUrl
    token: str


class DocumentTypeEnum(StrEnum):
    PASSPORT = auto()
    IDENTITY_CARD = auto()


class User(BaseUser):
    """
    A user of the application
    """

    avatar_url: HttpUrl
    birthday: date
    onboarding_completed: bool = False
    identity_verified: bool = False
    identity_document_type: DocumentTypeEnum | None = None
    identity_document_url: HttpUrl | None = None
    # Computed fields
    age: int
    is_minor: bool
    is_parent: bool
    # Related fields
    plan: PlanEnum
    linked_accounts: list[LinkedAccount] = Field(default_factory=list)

    @validator("age", always=True)
    def _age(cls, v, values, **kwargs):
        today = date.today()
        birthday = values["birthday"]
        age = (
            today.year
            - birthday.year
            - ((today.month, today.day) < (birthday.month, birthday.day))
        )
        return age

    @validator("is_minor", always=True)
    def _is_minor(cls, v, values, **kwargs):
        return values["age"] < 18


class UserMessagePermission(BaseModel):
    """
    A child's permission granted to his parent to read a given conversation
    """

    conversation_id: UUID4
    parent_id: UUID4


class UserActionHistory(BaseModel):
    """
    A record of an action performed by a user
    """

    id: UUID4
    user_id: UUID4
    timestamp: datetime
    title: str
    body: str


class Conversation(BaseModel):
    """
    Can be a post and its replies, or a conversation / channel / topic on a chat
    """

    id: UUID4
    platform: PlatformEnum


class Message(BaseLabelingModel):
    """
    A reply to a post or a message in a chat
    """

    source: PlatformEnum = Field(description="The source of the data")
