from enum import StrEnum, auto

from pydantic import BaseModel, validator


class SeverityEnum(StrEnum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()


class LabelEnum(StrEnum):
    IDENTITY_HATE = auto()
    INSULT = auto()
    OBSCENE = auto()
    THREAT = auto()
    TOXIC = auto()


class Label(BaseModel):
    label: LabelEnum
    severity: SeverityEnum
    score: float

    @validator("severity")
    def _severity(cls, value):
        SEVERITY_MAPPING = {
            LabelEnum.THREAT: SeverityEnum.HIGH,
            LabelEnum.IDENTITY_HATE: SeverityEnum.MEDIUM,
            LabelEnum.OBSCENE: SeverityEnum.MEDIUM,
            LabelEnum.INSULT: SeverityEnum.LOW,
            LabelEnum.TOXIC: SeverityEnum.LOW,
        }
        return SEVERITY_MAPPING[value]
