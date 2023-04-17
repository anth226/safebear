from datetime import datetime

import strawberry

from shared.models import Label

from .models import AdminUser


@strawberry.experimental.pydantic.type(model=Label, all_fields=True)
class LabelType:
    pass


@strawberry.type
class UnverifiedLabel:
    id: strawberry.ID
    label: LabelType
    message: str


@strawberry.type
class VerifiedLabel(UnverifiedLabel):
    verified_by: str
    verified_at: datetime


@strawberry.experimental.pydantic.type(name=AdminUser.__name__, model=AdminUser)
class AdminUserType:
    id: strawberry.auto
    first_name: strawberry.auto
    last_name: strawberry.auto
    email: strawberry.auto
    is_active: strawberry.auto
    created_at: strawberry.auto
    last_seen: strawberry.auto
