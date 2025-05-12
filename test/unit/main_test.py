import pytest
from main import setup


@pytest.fixture
def client():
    app = setup()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_api_data_missing_datetime(client):
    response = client.get("/api/data")
    assert response.status_code == 400
    assert response.is_json
    data = response.get_json()
    assert "Missing 'datetime'" in data.get("An error occurred", "")