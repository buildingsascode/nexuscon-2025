import requests
from requests.auth import HTTPBasicAuth


class DistechClient:
    base_url: str
    verify_cerficate: bool

    def __init__(
        self,
        username: str,
        password: str,
        base_url: str,
        verify_certificate: bool,
    ):
        self._username = username
        self._password = password
        self.base_url = base_url
        self.session = requests.sessions.Session()
        self.verify_cerficate = verify_certificate

        self._set_authentication_header()

    def _set_authentication_header(self):
        self.session.auth = HTTPBasicAuth(
            username=self._username, password=self._password
        )

    def get_resource(self) -> requests.Response:
        response = self.session.get(
            f"https://{self.base_url}/api/rest/v2/services/backup/backups",
            verify=self.verify_cerficate,
        )

        return response
