import os

import BAC0
import pytest
import pytest_asyncio
from BAC0.core.devices.Points import Point

from tools.templates.points import PointTemplate
from tools.templates.templates import get_template_points

BBMD_IP = os.environ["BBMD_IP"]
DISTECH_CONTROLLER = os.environ["DISTECH_DEVICE"]
DISTECH_CONTROLLER_DEVICE_ID = int(os.environ["BACNET_DEVICE_ID"])

BAC0.log_level("silence")


@pytest.fixture(scope="module")
def bbmd_ip() -> str:
    return os.environ["BBMD_IP"]


@pytest.fixture(scope="module")
def device_id() -> int:
    return int(os.environ["BACNET_DEVICE_ID"])


@pytest_asyncio.fixture(scope="module")
async def bacnet_device_points(bbmd_ip, device_id) -> list[Point]:
    bacnet = BAC0.lite(bbmdAddress=bbmd_ip, bbmdTTL=900)
    device = await BAC0.device(bbmd_ip, device_id, bacnet)
    points = device.points
    for point in points:
        _ = await point.value  # without this await subsequent reads seemed to fail
    return points


@pytest_asyncio.fixture(scope="module")
async def bacnet_device_points_by_name(bacnet_device_points) -> dict[str, Point]:
    return {point.properties.name: point for point in bacnet_device_points}


@pytest.fixture(scope="module")
def bacnet_template_points() -> list[PointTemplate]:
    return get_template_points()


@pytest.fixture(scope="module")
def bacnet_template_points_by_name(
    bacnet_template_points: list[PointTemplate],
) -> dict[str, PointTemplate]:
    return {point.name: point for point in bacnet_template_points}
