"""This CLI will be used to manage a Distech controller"""

from distech import setup_client


def main():
    print("Setting up client")
    client = setup_client()
    print("Restoring backup")
    client.restore_backup("latest")


if __name__ == "__main__":
    main()
