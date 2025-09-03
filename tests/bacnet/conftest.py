import BAC0
import pytest

DISTECH_CONTROLLER = "10.1.1.78:47808"
DISTECH_CONTROLLER_DEVICE_ID = 1000


@pytest.fixture
async def points():
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    bacnet_objects = await bacnet.read(f"{DISTECH_CONTROLLER} device {DISTECH_CONTROLLER_DEVICE_ID} objectName")