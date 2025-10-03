import pytest
from BAC0.core.devices.Points import Point

from tools.templates.points import BACnetObjectType, PointTemplate


@pytest.mark.asyncio
async def test_controller_point_names_in_template(
    bacnet_template_points_by_name,
    bacnet_device_points,
):
    for point in bacnet_device_points:
        assert (
            point.properties.name in bacnet_template_points_by_name
        ), f"Unexpected point name: {point.properties.name}"


@pytest.mark.asyncio
async def test_template_points_in_controller(
    bacnet_template_points_by_name: dict[str, PointTemplate],
    bacnet_device_points: list[Point],
):
    for point_name in bacnet_template_points_by_name:
        assert any(
            point.properties.name == point_name for point in bacnet_device_points
        ), f"Point {point_name} from template not found in controller points"


@pytest.mark.asyncio
async def test_point_type(
    bacnet_template_points_by_name: dict[str, PointTemplate],
    bacnet_device_points: list[Point],
):
    for point in bacnet_device_points:
        assert (
            point.properties.name is not None
        ), "Unable to test point type, point name is None"
        template_point = bacnet_template_points_by_name[point.properties.name]
        assert template_point.type == BACnetObjectType.from_bac0_type(
            point.properties.type
        ), f"Point type mismatch for point {point.properties.name}: template type {template_point.type}, controller type {point.properties.type}"
