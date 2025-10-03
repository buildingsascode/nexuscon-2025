from enum import Enum
from typing import NamedTuple


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
