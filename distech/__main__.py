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
    with open("test backup.zip", "wb") as backup_file:
        backup_file.write(backup)
    gfx_xml = client.extract_gfx_file(backup)
    with open(client.DEFAULT_GFX_FILE, "wb") as gfx_file:
        gfx_file.write(gfx_xml)


if __name__ == "__main__":
    main()
