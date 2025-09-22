"""This CLI will be used to manage a Distech controller"""

import os

from distech.client import DistechClient
from distech.models.backup import Backup


def main():
    client = DistechClient(
        base_url=os.environ["BBMD_IP"],
        username=os.environ["DISTECH_USER"],
        password=os.environ["DISTECH_PASS"],
        verify_certificate=False,
    )

    backups = client._get_resource(Backup)
    print(backups)

    # Run pytest verify controller is not working correctly

    # Restore correct version of controller program

    # Run pytest again to verify it works


if __name__ == "__main__":
    main()
