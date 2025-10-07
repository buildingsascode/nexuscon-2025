import pytest
from distech.client import DistechClient, setup_client

@pytest.fixture(scope="module")
def client() -> DistechClient:
    """Fixture to provide a DistechClient instance for integration tests"""
    return setup_client()