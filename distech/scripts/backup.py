"""This CLI will be used to manage a Distech controller"""

import datetime

from distech import setup_client


def main():
    print("Setting up client")
    client = setup_client()
    print("Backing up controller")
    backup = client.create_backup(
        "latest", option="full"
    )
    print(f"Backup job created: {backup.job}")


if __name__ == "__main__":
    main()
