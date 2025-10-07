import pytest
from BAC0.core.devices.Points import Point
from bacpypes3.basetypes import BinaryPV


@pytest.mark.asyncio
async def test_switch_off_led_off(
    bacnet_device_points_by_name: dict[str, Point],
):
    switch_input = bacnet_device_points_by_name["LEDInputSwitch"]
    if await switch_input.value == BinaryPV.active:
        pytest.skip("Switch is on, skipping test")
    led_output = bacnet_device_points_by_name["LEDOutput"]
    assert await led_output.value == 0.0, "LED should be off when switch is off"


@pytest.mark.asyncio
async def test_switch_on_led_on(
    bacnet_device_points_by_name: dict[str, Point],
):
    switch_input = bacnet_device_points_by_name["LEDInputSwitch"]
    if await switch_input.value == BinaryPV.inactive:
        pytest.skip("Switch is off, skipping test")
    led_output = bacnet_device_points_by_name["LEDOutput"]
    assert await led_output.value == 100.0, "LED should be on when switch is"
