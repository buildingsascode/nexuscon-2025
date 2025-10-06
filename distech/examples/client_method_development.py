"""Example script for client method development and testing"""

from distech.client import setup_client


def main():
    client = setup_client()
    client.upload_backup(
        "demos/as_builts/building_0001/space_123/eclypse-9a65e1.zip"
    )


if __name__ == "__main__":
    main()
