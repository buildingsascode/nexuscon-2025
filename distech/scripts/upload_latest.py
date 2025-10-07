from distech.client import setup_client


def main():
    print("Setting up client")
    client = setup_client()
    print("Uploading latest backup")
    client.upload_backup("demos/as_builts/building_0001/space_123/latest.zip")
    print("Latest backup uploaded")

if __name__ == "__main__":
    main()
