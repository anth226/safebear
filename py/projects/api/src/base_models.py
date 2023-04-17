from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr, Field, SecretStr, validator


class BaseUser(BaseModel):
    id: UUID4
    email: EmailStr
    password: SecretStr
    first_name: str
    last_name: str
    is_active: bool = True
    last_seen: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Computed fields
    full_name: str

    @validator("full_name", always=True)
    def _full_name(cls, v, values, **kwargs):
        return "{first_name} {last_name}".format(**values)


class BaseLabelingModel(BaseModel):
    """
    A base class for labeling messages
    """

    id: UUID4
    conversation_id: UUID4
    source: str = Field(description="The platform on which the message originated")
    author_id: str = Field(description="The author's identifier on that Platform")
    timestamp: datetime
    body: str
    # Toxiciy labels
    identity_hate: float
    is_identity_hate: bool
