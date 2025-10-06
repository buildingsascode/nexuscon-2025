"""This CLI will be used to manage a Distech controller"""

from distech import setup_client


def main():
    print("Setting up client")
    client = setup_client()
    print("Backing up controller")
    client.restore_backup("test backup")


if __name__ == "__main__":
    main()
