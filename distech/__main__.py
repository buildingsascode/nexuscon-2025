"""This CLI will be used to manage a Distech controller"""

import os
from pathlib import Path

from distech import DistechClient
from distech.models.backup import Backup

UNVERSIONED_FILES = Path("demos/as_builts/building_0001/space_001")
VERSIONED_FILES = Path("demos/as_builts/building_0001/space_123")


def get_latest_backup(client: DistechClient) -> Backup:
    backups = client.get_backups()
    backup = max(backups, key=lambda b: b.creation_time)

    return backup


def get_gfx_file(client: DistechClient, backup: bytes) -> bytes:
    gfx_xml = client.extract_gfx_file(backup)
    return gfx_xml


def setup_client() -> DistechClient:
    return DistechClient(
        base_url=os.environ["DISTECH_DEVICE"],
        username=os.environ["DISTECH_USER"],
        password=os.environ["DISTECH_PASS"],
        verify_certificate=False,
    )


def write_unversioned_files(
    client: DistechClient,
    latest_backup: Backup,
    backup: bytes,
) -> None:
    """Many organizations are not using version control and instead rely on multiple files with different names, this function writes files with inconsistent names."""
    backup_path = Path(
        UNVERSIONED_FILES,
        f"{client.base_url}_{latest_backup.creation_time.strftime('%Y%m%d_%H%M%S')}.zip",
    )
    with open(backup_path, "wb") as backup_file:
        backup_file.write(backup)
    gfx = get_gfx_file(client, backup)
    with open(Path(UNVERSIONED_FILES, client.DEFAULT_GFX_FILE), "wb") as gfx_file:
        gfx_file.write(gfx)


def write_versioned_files(
    client: DistechClient,
    backup: bytes,
) -> None:
    """Some organization use version control and want to keep a single file name, this function writes files with consistent names."""
    backup_path = Path(VERSIONED_FILES, f"{client.base_url}.zip")
    with open(backup_path, "wb") as backup_file:
        backup_file.write(backup)
    gfx = get_gfx_file(client, backup)
    with open(Path(VERSIONED_FILES, client.DEFAULT_GFX_FILE), "wb") as gfx_file:
        gfx_file.write(gfx)


def main():
    client = setup_client()
    latest_backup = get_latest_backup(client)
    backup = client.download_backup(latest_backup.key)
    write_unversioned_files(client, latest_backup, backup)
    write_versioned_files(client, backup)


if __name__ == "__main__":
    main()
