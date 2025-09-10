import BAC0
import pytest
import pytest_asyncio
from BAC0.core.devices.Points import Point

from distech.constants import DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID
from tools.templates.points import PointTemplate
from tools.templates.templates import get_template_points


@pytest.fixture(scope="module")
def bacnet_template_points() -> list[PointTemplate]:
    return get_template_points()


@pytest.fixture(scope="module")
def bacnet_template_points_by_name(bacnet_template_points) -> dict[str, PointTemplate]:
    return {point.name: point for point in bacnet_template_points}


@pytest_asyncio.fixture(scope="module")
async def bacnet_device_points() -> list[Point]:
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    device = await BAC0.device(DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID, bacnet)
    points = device.points
    return points


@pytest.mark.asyncio
async def test_controller_point_names_in_template(
    bacnet_template_points_by_name, bacnet_device_points
):
    for point in bacnet_device_points:
        assert (
            point.properties.name in bacnet_template_points_by_name
        ), f"Unexpected point name: {point.properties.name}"


@pytest.mark.asyncio
async def test_template_points_in_controller(
    bacnet_template_points_by_name, bacnet_device_points
):
    for point_name in bacnet_template_points_by_name:
        assert any(
            point.properties.name == point_name for point in bacnet_device_points
        ), f"Point {point_name} from template not found in controller points"


@pytest.mark.asyncio
async def test_point_units(bacnet_template_points_by_name): ...
