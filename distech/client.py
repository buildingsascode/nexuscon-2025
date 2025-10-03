import io
import os
import zipfile
from typing import Type, TypeVar
from zipfile import ZipFile

import requests
import urllib3
from requests.auth import HTTPBasicAuth

from distech.models import Backup, Job
from distech.models.distech import DistechResource

T = TypeVar("T", bound=DistechResource)


class DistechClient:
    DEFAULT_GFX_FILE: str = "Main.xml"
    base_url: str
    verify_tls: bool

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        verify_certificate: bool,
    ):
        self.base_url = base_url
        self.session = requests.sessions.Session()
        self.verify_tls = verify_certificate
        self._set_authentication_header(username, password)
        if not self.verify_tls:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def _set_authentication_header(
        self,
        username: str,
        password: str,
    ) -> None:
        """Set the authentication header for the session"""
        self.session.auth = HTTPBasicAuth(username, password)

    def _get_resources(self, resource: Type[T]) -> list[T]:
        """Generic method to get a resource from the Distech controller"""
        response = self.session.get(
            f"https://{self.base_url}{resource.get_endpoint()}",
            verify=self.verify_tls,
        )
        response.raise_for_status()
        raw_response = response.json()
        if isinstance(raw_response, dict):
            response = [resource.model_validate(item) for item in raw_response.values()]
        else:
            raise ValueError("Unexpected response format")
        return response

    def _get_resource(self, resource: Type[T]) -> T:
        """Generic method to get a single resource from the Distech controller"""
        response = self.session.get(
            f"https://{self.base_url}{resource.get_endpoint()}",
            verify=self.verify_tls,
        )
        response.raise_for_status()
        raw_response = response.json()
        if isinstance(raw_response, dict):
            response = resource.model_validate(raw_response)
        else:
            raise ValueError("Unexpected response format")
        return response

    def create_backup(self, name: str, option: str) -> Job:
        """Create a new backup on the Distech controller"""
        response = self.session.post(
            f"https://{self.base_url}/api/rest/v2/services/backup/backups/create",
            verify=self.verify_tls,
            json={
                "item": name,
                "option": option,
            },
        )
        response.raise_for_status()
        raw_response = response.json()
        if isinstance(raw_response, dict):
            response = Job.model_validate(raw_response)
        else:
            raise ValueError("Unexpected response format")
        return response

    def get_backups(self) -> list[Backup]:
        """Get the list of backups from the Distech controller"""
        return self._get_resources(Backup)

    def download_backup(
        self,
        key: str,
    ) -> bytes:
        """Download a backup from the Distech controller"""
        response = self.session.get(
            f"https://{self.base_url}/api/rest/v2/services/backup/store/{key}",
            verify=self.verify_tls,
        )
        response.raise_for_status()
        return response.content

    def is_valid_backup(
        self,
        zip_file: ZipFile,
    ) -> bool:
        """Checks a zip file to see if it is a valid Distech backup file"""
        # TODO this function should be more robust
        if not isinstance(zip_file, ZipFile):
            raise ValueError("Expected a ZipFile instance")
        REQUIRED_FILES = {
            "META-INF/manifest.json",
            "bundle-content/com.distech.dcaf.core.gfx/files/project/Project.gfx",
        }
        zip_contents = set(file.filename for file in zip_file.filelist)
        return REQUIRED_FILES.issubset(zip_contents)

    def extract_gfx_file(
        self,
        backup: bytes,
    ) -> bytes:
        """Extract the Project.gfx file from a Distech backup zip file"""
        if zipfile.is_zipfile(io.BytesIO(backup)) is False:
            raise ValueError("Invalid zip file")
        zip_file = ZipFile(io.BytesIO(backup))
        if self.is_valid_backup(zip_file) is False:
            raise ValueError("Invalid Distech backup file")
        gfx_bytes = zip_file.open(
            "bundle-content/com.distech.dcaf.core.gfx/files/project/Project.gfx"
        ).read()
        gfx_zip = ZipFile(io.BytesIO(gfx_bytes))
        gfx_xml = gfx_zip.open(self.DEFAULT_GFX_FILE).read()
        gfx_zip.close()
        return gfx_xml

    def get_latest_backup(self) -> Backup:
        backups = self.get_backups()
        backup = max(backups, key=lambda b: b.creation_time)

        return backup

    def get_gfx_file(self, backup: bytes) -> bytes:
        gfx_xml = self.extract_gfx_file(backup)
        return gfx_xml


def setup_client() -> DistechClient:
    return DistechClient(
        base_url=os.environ["DISTECH_DEVICE"],
        username=os.environ["DISTECH_USER"],
        password=os.environ["DISTECH_PASS"],
        verify_certificate=False,
    )
