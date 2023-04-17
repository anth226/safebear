"""
Shared types between the app and the admin APIs
"""
import strawberry

from shared.models import LabelEnum, SeverityEnum

Label = strawberry.enum(_cls=LabelEnum, name="Label", description="A toxicity label")

Severity = strawberry.enum(
    _cls=SeverityEnum, name="Severity", description="Severity of a toxicity label"
)
