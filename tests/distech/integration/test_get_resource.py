from distech.client import DistechClient
from distech.models.backup import Backup


def test_get_resources(client: DistechClient):
    """Test listing backups"""
    backups = client.get_backups()
    assert isinstance(backups, list)
    assert all(isinstance(backup, Backup) for backup in backups)
    assert len(backups) > 0


def test_get_resource(client: DistechClient):
    """Test getting the latest backup"""
    backup = client.get_latest_backup()
    assert isinstance(backup, Backup)