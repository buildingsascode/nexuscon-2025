import asyncio
import os

import BAC0


async def main():
    bacnet = BAC0.lite(bbmdAddress=os.environ["BBMD_IP"], bbmdTTL=900)
    await bacnet._write(
        f"{os.environ["DISTECH_DEVICE"]} binaryInput 101 presentValue active"
    )


if __name__ == "__main__":
    asyncio.run(main())
