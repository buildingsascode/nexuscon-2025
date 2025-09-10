from typing import Annotated, Literal

from pydantic import BaseModel, BeforeValidator, Field, PlainSerializer


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
    name: str = Field(..., alias="POINT NAME")
    description: str | None = Field(..., alias="POINT DESCRIPTION")
    hardware_software: Literal["HARDWARE", "SOFTWARE"] = Field(
        ..., alias="HARDWARE/SOFTWARE"
    )
    type: Literal["AO", "AI", "BO", "BI", "AVO", "AVI", "BVO", "BVI"] = Field(
        ..., alias="POINT TYPE"
    )
    value_type: Literal["Numeric", "Boolean"] = Field(..., alias="VALUE TYPE")
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
    ] = Field(..., alias="UNITS")
    trend: XToBool = Field(..., alias="TREND")
    cov_interval: str = Field(..., alias="COV/INTERVAL")
    alarm: XToBool = Field(..., alias="ALARM")
    alarm_priority: int | None = Field(..., alias="ALARM PRIORITY", ge=1, le=5)
    show_on_graphic: XToBool = Field(..., alias="SHOW ON GRAPHIC")
    tags: str = Field(..., alias="TAGS")
