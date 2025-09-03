import asyncio

import BAC0

DISTECH_CONTROLLER = "10.1.1.78:47808"
DISTECH_CONTROLLER_DEVICE_ID = 1000


async def main():
    print("Setting up BAC0")
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    device = await BAC0.device(DISTECH_CONTROLLER, DISTECH_CONTROLLER_DEVICE_ID, bacnet)
    points = device.points
    point = points[0]

if __name__ == "__main__":
    asyncio.run(main())
