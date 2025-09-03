import asyncio

import BAC0

DISTECH_CONTROLLER = "192.168.1.100:47808"
DISTECH_CONTROLLER_DEVICE_ID = 1000

async def main():
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER)
    bacnet.discover(
        limits=(DISTECH_CONTROLLER_DEVICE_ID, DISTECH_CONTROLLER_DEVICE_ID), global_broadcast=True
    )
    present_value = await bacnet.read(f"{DISTECH_CONTROLLER} analogValue {DISTECH_CONTROLLER_DEVICE_ID} objectList")
    print(f"Present Value: {present_value}")


if __name__ == "__main__":
    asyncio.run(main())
