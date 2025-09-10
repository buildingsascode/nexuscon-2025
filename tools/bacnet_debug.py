import asyncio

import BAC0
from bacpypes3.primitivedata import ObjectIdentifier

from distech.constants import DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID


async def get_object_list(bacnet, device_id) -> list:
    bacnet_objects = await bacnet.read(
        f"{DISTECH_CONTROLLER} device {device_id} objectList"
    )
    return bacnet_objects


async def main():
    print("Setting up BAC0")
    BAC0.log_level("silence")
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    device = await BAC0.device(DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID, bacnet)
    bacnet_objects: list[ObjectIdentifier] = await get_object_list(
        bacnet, DISTECH_CONTROLLER_DEVICE_ID
    )

    for bacnet_object in bacnet_objects:
        print(await bacnet.read(f"{DISTECH_CONTROLLER} {bacnet_object} objectName"))


if __name__ == "__main__":
    asyncio.run(main())
