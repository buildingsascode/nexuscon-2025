"""This CLI will be used to manage a Distech controller"""

import os
from pathlib import Path

from distech import DistechClient

DEMO_FILES = Path("./demos/as_builts/building_0001/space_001")


def get_latest_backup(client: DistechClient) -> None:
    backups = client.get_backups()
    print(f"Found {len(backups)} backups")
    latest_backup = max(backups, key=lambda b: b.creation_time)
    backup = client.download_backup(latest_backup.key)
    backup_path = Path(
        DEMO_FILES,
        f"{client.base_url}_{latest_backup.creation_time.strftime('%Y%m%d_%H%M%S')}.zip",
    )
    with open(backup_path, "wb") as backup_file:
        backup_file.write(backup)
    get_gfx_file(client, backup)


def get_gfx_file(client: DistechClient, backup: bytes) -> None:
    gfx_xml = client.extract_gfx_file(backup)
    with open(Path(DEMO_FILES, client.DEFAULT_GFX_FILE), "wb") as gfx_file:
        gfx_file.write(gfx_xml)


def setup_client() -> DistechClient:
    return DistechClient(
        base_url=os.environ["DISTECH_DEVICE"],
        username=os.environ["DISTECH_USER"],
        password=os.environ["DISTECH_PASS"],
        verify_certificate=False,
    )


def main():
    client = setup_client()
    get_latest_backup(client)


if __name__ == "__main__":
    main()
