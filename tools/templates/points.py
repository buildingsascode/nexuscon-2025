from enum import Enum
from typing import Annotated, Literal, NamedTuple

from bacpypes3.basetypes import EngineeringUnits
from pydantic import BaseModel, BeforeValidator, Field, PlainSerializer, field_validator


class BACnetType(NamedTuple):
    point_type: str
    description: str
    bac0_type: str


class BACnetObjectType(BACnetType, Enum):
    AO = "AO", "Analog Output", "analog-output"
    AI = "AI", "Analog Input", "analog-input"
    BO = "BO", "Binary Output", "binary-output"
    BI = "BI", "Binary Input", "binary-input"
    AVO = "AVO", "Analog Value Output", "analog-value"
    AVI = "AVI", "Analog Value Input", "analog-value"
    BVO = "BVO", "Binary Value Output", "binary-value"
    BVI = "BVI", "Binary Value Input", "binary-value"

    @classmethod
    def from_bac0_type(cls, bac0_type: str) -> "BACnetObjectType":
        for obj in cls:
            if obj.bac0_type == bac0_type:
                return obj
        raise ValueError(f"Unknown point type: {bac0_type}", bac0_type)


class BACnetUnit(NamedTuple):
    unit: str
    description: str
    bac0_unit: int


class BACnetObjectUnit(BACnetUnit, Enum):
    PERCENT = "%", "Percent", EngineeringUnits.percent
    DEG_F = "°F", "Degrees Fahrenheit", EngineeringUnits.degreesFahrenheit
    AMPERE = "A", "Amperes", EngineeringUnits.amperes
    BOOLEAN = "FALSE,TRUE", "Boolean", None
    HERTZ = "Hz", "Hertz", EngineeringUnits.hertz
    LB_H = "lb/h", "Pounds per hour", EngineeringUnits.poundsMassPerHour
    NORMAL_FAULT = "NORMAL,FAULT", "Normal/Fault", EngineeringUnits.noUnits
    OFF_ON = "OFF,ON", "Off/On", EngineeringUnits.noUnits
    PSI = "psi", "Pounds per square inch", EngineeringUnits.poundsForcePerSquareInch
    STOPPED_STARTED = "STOPPED,STARTED", "Stopped/Started", EngineeringUnits.noUnits

    @classmethod
    def from_bac0_unit(cls, bac0_unit: EngineeringUnits) -> "BACnetObjectUnit":
        for unit in cls:
            if unit.bac0_unit == bac0_unit:
                return unit
        raise ValueError(f"Unknown unit: {bac0_unit}", bac0_unit)


def _x_to_bool(input: str | bool | None) -> bool:
    match input:
        case bool():
            return input
        case "X":
            return True
        case "":
            return False
        case None:
            return False
        case _:
            raise ValueError(f"Could not convert {input} to boolean", input)


def bool_to_x(input: bool) -> str:
    match input:
        case True:
            return "X"
        case False:
            return ""
        case _:
            raise ValueError(
                f"Could not convert {input} to Yes No Picklist value", input
            )


XToBoolSerializer: PlainSerializer = PlainSerializer(bool_to_x, return_type=str)
XToBoolValidator: BeforeValidator = BeforeValidator(_x_to_bool)
XToBool = Annotated[bool, XToBoolSerializer, XToBoolValidator]
__all__ = ["XToBool"]


class PointTemplate(BaseModel):
    name: str = Field(alias="POINT NAME")
    description: str | None = Field(alias="POINT DESCRIPTION")
    hardware_software: Literal["HARDWARE", "SOFTWARE"] = Field(
        alias="HARDWARE/SOFTWARE"
    )
    type: BACnetObjectType = Field(alias="POINT TYPE")
    value_type: Literal["Numeric", "Boolean"] = Field(alias="VALUE TYPE")
    units: BACnetObjectUnit = Field(alias="UNITS")
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

    @field_validator("units", mode="before")
    @classmethod
    def parse_units(cls, v):
        if isinstance(v, BACnetObjectUnit):
            return v
        try:
            return BACnetObjectUnit[v]
        except KeyError:
            raise ValueError(f"Invalid BACnetObjectUnit: {v}")
