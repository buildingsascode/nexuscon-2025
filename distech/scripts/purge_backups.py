from distech.client import setup_client


def main():
    print("Setting up client")
    client = setup_client()
    print("Getting all backups")
    backups = client.get_backups()
    print(f"Found {len(backups)} backups")
    for backup in backups:
        print(f"Deleting backup: [{backup.key}] created at {backup.creation_time}")
        client.delete_backup(backup.key)
    print("All backups deleted")


if __name__ == "__main__":
    main()
