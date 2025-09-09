import asyncio

import BAC0
from BAC0.core.devices.Device import Device

from distech.constants import DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID


async def main():
    print("Setting up BAC0")
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    device = await BAC0.device(DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID, bacnet)

    get_points(device)


def get_points(device: Device):
    """Workaround for a bug in BAC0"""
    point_count = len(device.points)
    points = list()
    for i in range(point_count):
        points.append(device.points[i])
    return points


if __name__ == "__main__":
    asyncio.run(main())
