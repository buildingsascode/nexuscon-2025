import asyncio

import BAC0
from BAC0.core.devices import Points

from distech.constants import DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID


async def main():
    print("Setting up BAC0")
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    device = await BAC0.device(DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID, bacnet)
    await asyncio.sleep(1)
    points: list[Points.Point] = device.points
    print(device.points)
    for point in points:
        print(
            f"Point: {point.properties.name=}, {point.properties.address}, {point.tags=}, {point.units=}, {await point.value=}, {point.status=}, {point.properties.description=}, {point.properties.type=}"
        )


if __name__ == "__main__":
    asyncio.run(main())
