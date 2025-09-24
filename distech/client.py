from typing import Sequence, Type, TypeVar

import requests
from requests.auth import HTTPBasicAuth

from distech.models import Backup
from distech.models.distech import DistechResource

T = TypeVar("T", bound=DistechResource)


class DistechClient:
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

    def get_backups(self) -> list[Backup]:
        """Get the list of backups from the Distech controller"""
        return self._get_resources(Backup)

    def download_backup(self, id_: str) -> bytes:
        """Download a backup from the Distech controller"""
        response = self.session.get(
            f"https://{self.base_url}/api/rest/v2/services/backup/backups/{id_}/download",
            verify=self.verify_tls,
        )

        response.raise_for_status()
        return response.content

    def get_programs(self) -> Sequence[str]:
        """Get the list of programs from the Distech controller"""
        response = self.session.get(
            f"https://{self.base_url}/api/rest/v2/services/programs/programs/",
            verify=self.verify_tls,
        )

        response.raise_for_status()
        raw_response = response.json()
        if isinstance(raw_response, dict):
            programs = list(raw_response.keys())
        else:
            raise ValueError("Unexpected response format")

        return programs
