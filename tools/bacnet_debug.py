import asyncio
import os

import BAC0
from BAC0.core.devices import Points


async def main():
    print("Setting up BAC0")
    bacnet = BAC0.lite(bbmdAddress=os.environ["BBMD_IP"], bbmdTTL=900)
    device = await BAC0.device(
        os.environ["DISTECH_DEVICE"], os.environ["BACNET_DEVICE_ID"], bacnet
    )
    points: list[Points.Point] = device.points
    print(device.points)
    for point in points:
        print(
            f"Point: {point.properties.name=}, {point.properties.address}, {point.tags=}, {point.units=}, {await point.value=}, {point.status=}, {point.properties.description=}, {point.properties.type=}"
        )


if __name__ == "__main__":
    asyncio.run(main())
