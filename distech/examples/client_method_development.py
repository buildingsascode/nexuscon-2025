"""Example script for client method development and testing"""

from distech.client import setup_client


def main():
    client = setup_client()
    print(client.list_programs())
    print(client.list_program(program_id="1"))


if __name__ == "__main__":
    main()
