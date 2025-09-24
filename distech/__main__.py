"""This CLI will be used to manage a Distech controller"""

import os

from distech import DistechClient


def main():
    client = DistechClient(
        base_url=os.environ["BBMD_IP"],
        username=os.environ["DISTECH_USER"],
        password=os.environ["DISTECH_PASS"],
        verify_certificate=False,
    )

    backups = client.get_backups()
    print(f"Found {len(backups)} backups")
    for backup in backups:
        print(f"- {backup.key=} {backup.size=} backup.creation_time={backup.creation_time.strftime('%Y-%m-%d %H:%M:%S')}")

    # Run pytest verify controller is not working correctly

    # Restore correct version of controller program

    # Run pytest again to verify it works


if __name__ == "__main__":
    main()
