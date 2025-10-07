from typing import Literal

from pydantic import BaseModel, Field, field_validator

from tools.templates.bacnet_object_type import BACnetObjectType
from tools.templates.serializers import XToBool


class PointTemplate(BaseModel):
    name: str = Field(alias="POINT NAME")
    description: str | None = Field(alias="POINT DESCRIPTION")
    hardware_software: Literal["HARDWARE", "SOFTWARE"] = Field(
        alias="HARDWARE/SOFTWARE"
    )
    type: BACnetObjectType = Field(alias="POINT TYPE")
    value_type: Literal["Numeric", "Boolean"] = Field(alias="VALUE TYPE")
    units: Literal[
        "%",
        "°F",
        "A",
        "FALSE,TRUE",
        "Hz",
        "kBTU/h",
        "lb/h",
        "NORMAL,FAULT",
        "OFF,ON",
        "psi",
        "STOPPED,STARTED",
    ] = Field(alias="UNITS")
    trend: XToBool = Field(alias="TREND")
    cov_interval: str = Field(alias="COV/INTERVAL")
    alarm: XToBool = Field(alias="ALARM")
    alarm_priority: int | None = Field(alias="ALARM PRIORITY", ge=1, le=5)
    show_on_graphic: XToBool = Field(alias="SHOW ON GRAPHIC")
    tags: str = Field(alias="TAGS")

    @field_validator("type", mode="before")
    @classmethod
    def parse_type(cls, v):
        if isinstance(v, BACnetObjectType):
            return v
        try:
            return BACnetObjectType[v]
        except KeyError:
            raise ValueError(f"Invalid BACnetObjectType: {v}")
