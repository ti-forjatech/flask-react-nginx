import pytest

from server.create_app import create_app


@pytest.fixture
def client():
    application = create_app()
    client = application.test_client()
    yield client


def test_routes(client):
    response = client.get("/app/data")
    assert response.status_code == 200
    response = client.get("/app/login")
    assert response.status_code == 200
