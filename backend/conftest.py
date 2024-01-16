import pytest
from fastapi.testclient import TestClient
from utils.singleton_instances import app as real_app


@pytest.fixture(scope="session")
def test_client():
    client = TestClient(real_app)
    yield client
