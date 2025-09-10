import BAC0
import pytest
from BAC0.core.devices.Points import Point

from distech.constants import DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID
from tools.templates.points import PointTemplate
from tools.templates.templates import get_template_points


@pytest.fixture(scope="module")
def bacnet_template_points() -> list[PointTemplate]:
    return get_template_points()


@pytest.fixture(scope="module")
def bacnet_template_points_by_name(bacnet_points) -> dict[str, PointTemplate]:
    return {point.name: point for point in bacnet_points}


@pytest.mark.asyncio
async def test_point_names(bacnet_template_points_by_name):
    print("Setting up BAC0")
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    device = await BAC0.device(DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID, bacnet)
    points: list[Point] = device.points
    for point in points:
        assert (
            point.properties.name in bacnet_template_points_by_name
        ), f"Unexpected point name: {point.properties.name}"
