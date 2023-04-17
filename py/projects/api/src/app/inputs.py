from datetime import date

import strawberry
from pydantic import BaseModel, EmailStr, Field, SecretStr, validator

from ._types import DocumentType


class RegisterInputModel(BaseModel):
    email: EmailStr = Field(description="User's email address")
    first_name: str = Field(description="User's first name")
    last_name: str = Field(description="User's last name")
    birthday: date = Field(description="User's birthday")
    password: SecretStr = Field(description="User's password")
    password_confirmation: str = Field(description="User's password confirmation")

    @validator("password")
    def password_validation(cls, v, values, **kwargs):
        if len(v.get_secret_value()) < 8:
            raise ValueError("password must be at least 8 characters long")
        if not any(char.isdigit() for char in v.get_secret_value()):
            raise ValueError("password must contain at least 1 digit")
        if not any(char.isupper() for char in v.get_secret_value()):
            raise ValueError("password must contain at least 1 uppercase letter")
        return v

    @validator("password_confirmation")
    def passwords_match(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords do not match")
        return v


@strawberry.experimental.pydantic.input(
    model=RegisterInputModel,
    all_fields=True,
    name=RegisterInputModel.__name__,
    description="The toxicity evaluation of a given message",
)
class RegisterInput:
    pass


@strawberry.input
class UserInvitationInput:
    token: str | None = strawberry.field(
        description=(
            "One-time invitation token that is used to link a child to a parent's"
            " account"
        )
    )
    email: str | None = strawberry.field(description="Child's email adress")


@strawberry.input
class UploadIdentityDocumentInput:
    path: str = strawberry.field(description="Path to the document's image on S3")
    type: DocumentType


@strawberry.input
class UpdateProfileInput:
    first_name: str | None = strawberry.UNSET
    last_name: str | None = strawberry.UNSET
    email: str | None = strawberry.UNSET
    onboarding_completed: bool | None = strawberry.UNSET
    password: str | None = strawberry.UNSET
    password_confirmation: str | None = strawberry.UNSET
