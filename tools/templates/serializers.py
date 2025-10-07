from typing import Annotated

from pydantic import BeforeValidator, PlainSerializer


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
