import pytest
from requests import HTTPError

from distech.client import DistechClient


def test_request_404_raises_httperror(client: DistechClient):
    """Test handling of request that results in a 404 error"""
    pytest.raises(HTTPError, client.list_program, "INVALID_KEY")
