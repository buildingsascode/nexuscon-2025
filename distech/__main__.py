"""This CLI will be used to manage a Distech controller"""

import os

from distech.client import DistechClient


def main():
    client = DistechClient(
        base_url=os.environ["BBMD_IP"],
        username=os.environ["DISTECH_USER"],
        password=os.environ["DISTECH_PASS"],
        verify_certificate=False,
    )

    backups = client.get_backups()
    print(backups.json())


if __name__ == "__main__":
    main()


test = {
    "test backup": {
        "key": "test backup",
        "size": 44041,
        "creation-time": "2025-09-19T20:24:08Z",
        "includes": ["DeviceIdentity", "Designer", "AlarmsTrends"],
        "packages": {
            "com.distech.dcaf.web.widgets": {
                "key": "com.distech.dcaf.web.widgets",
                "vendor": "Distech Controls",
                "version": "2.8.4+25212.1",
            },
            "com.distech.dcaf.modbus": {
                "key": "com.distech.dcaf.modbus",
                "vendor": "Distech Controls",
                "version": "2.8.4+25197.3",
            },
            "com.distech.dcaf.bacnet": {
                "key": "com.distech.dcaf.bacnet",
                "vendor": "Distech Controls",
                "version": "2.8.4+25205.1",
            },
            "com.distech.dcaf.iot": {
                "key": "com.distech.dcaf.iot",
                "vendor": "Distech Controls",
                "version": "2.8.4+25197.3",
            },
            "com.distech.dcaf.mbus": {
                "key": "com.distech.dcaf.mbus",
                "vendor": "Distech Controls",
                "version": "2.8.4+25197.3",
            },
            "com.distech.dcaf.webinterface": {
                "key": "com.distech.dcaf.webinterface",
                "vendor": "Distech Controls",
                "version": "2.8.4+25212.1",
            },
            "com.distech.os": {
                "key": "com.distech.os",
                "vendor": "Distech Controls",
                "version": "2.8.4+25224.1",
            },
            "com.distech.dcaf.subnet": {
                "key": "com.distech.dcaf.subnet",
                "vendor": "Distech Controls",
                "version": "2.8.4+25217.1",
            },
            "com.distech.dcaf.remotetunneling": {
                "key": "com.distech.dcaf.remotetunneling",
                "vendor": "Distech Controls",
                "version": "2.8.4+25197.3",
            },
            "com.distech.dcaf.extensioniomodule": {
                "key": "com.distech.dcaf.extensioniomodule",
                "vendor": "Distech Controls",
                "version": "2.8.4+25197.3",
            },
            "com.distech.dcaf": {
                "key": "com.distech.dcaf",
                "vendor": "Distech Controls",
                "version": "2.8.4+25212.1",
            },
            "com.distech.dcaf.weather": {
                "key": "com.distech.dcaf.weather",
                "vendor": "Distech Controls",
                "version": "2.8.4+25197.3",
            },
            "com.distech.dcaf.mqtt": {
                "key": "com.distech.dcaf.mqtt",
                "vendor": "Distech Controls",
                "version": "2.8.4+25197.3",
            },
        },
        "platform": {
            "os-version": "2025.2.1-34-gea606ad",
            "framework-version": "33.0.0.17",
            "jvm-version": "17.0.14",
            "model-id": "10016C0005820418",
            "model-name": "ECY-303-BI",
            "model-revision": "1.0A",
            "host-id": "ECY303-B0FA3DD5-F776-50A9-89D6-02CC6905D21D",
            "vendor-name": "Distech Controls Inc.",
            "units": "Us",
            "architecture": "arm",
            "kernel-version": "v6.12.19",
        },
    }
}
