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
        print(
            f"- {backup.key=} {backup.size=} backup.creation_time={backup.creation_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )

    backup = client.download_backup("test backup")
    if not client.is_valid_backup(backup):
        raise ValueError("Unexpected backup content ")
    


if __name__ == "__main__":
    main()
