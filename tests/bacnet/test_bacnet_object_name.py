import BAC0
import pytest
from BAC0.core.devices.Points import Point

from distech.constants import DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID

EXPECTED_POINT_NAMES = {"LEDOutput", "LEDInputSwitchh"}

point = Point(pointName="LEDOutput")

@pytest.mark.asyncio
async def test_point_names():
    print("Setting up BAC0")
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    device = await BAC0.device(DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID, bacnet)
    points: list[Point] = device.points
    for point in points:
        assert (
            point.properties.name in EXPECTED_POINT_NAMES
        ), f"Unexpected point name: {point.properties.name}"
