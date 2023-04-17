from pydantic import BaseModel, Field, create_model

from .models import LabelEnum


class InferenceInput(BaseModel):
    """
    Request schema for the toxicity inference endpoint
    """

    message: str


InferenceOutput = create_model(
    "InferenceOutput",
    __doc__="Response schema for the toxicity inference endpoint",
    **{label.name: (Field(ge=0, le=1), ...) for label in LabelEnum},
)
