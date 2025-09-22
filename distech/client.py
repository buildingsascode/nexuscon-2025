import requests
from requests.auth import HTTPBasicAuth


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
        self.session.auth = HTTPBasicAuth(username, password)

    def get_backups(self) -> requests.Response:
        response = self.session.get(
            f"https://{self.base_url}/api/rest/v2/services/backup/backups",
            verify=self.verify_tls,
        )

        return response

    