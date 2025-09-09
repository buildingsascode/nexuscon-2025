import asyncio

import BAC0

from distech.constants import DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID


async def main():
    print("Setting up BAC0")
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    device = await BAC0.device(DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID, bacnet)
    object_list = await bacnet.read(
        f"{DISTECH_CONTROLLER} device {DISTECH_CONTROLLER_DEVICE_ID} objectList"
    )
    print(object_list)


if __name__ == "__main__":
    asyncio.run(main())
