"""This CLI will be used to manage a Distech controller"""

import os

from distech.client import DistechClient


def main():
    client = DistechClient(
        base_url=os.environ["BBMD_IP"],
        username=os.environ["DISTECH_USER"],
        password=os.environ["DISTECH_PASS"],
        verify_certificate=False,
    )

    resource = client.get_resource()


if __name__ == "__main__":
    main()
