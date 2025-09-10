import asyncio

import BAC0

from distech.constants import DISTECH_CONTROLLER


async def main():
    bacnet = BAC0.lite(bbmdAddress=DISTECH_CONTROLLER, bbmdTTL=900)
    await bacnet._write(f"{DISTECH_CONTROLLER} binaryInput 101 presentValue active")


if __name__ == "__main__":
    asyncio.run(main())
