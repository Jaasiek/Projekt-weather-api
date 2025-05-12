from datetime import datetime, timedelta
import pytest
from main import setup


@pytest.fixture
def client():
    app = setup()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_api_data_missing_datetime(client) -> None:
    response = client.get("/api/data")
    assert response.status_code == 400


def test_api_data_post_success(client) -> None:
    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "pm10": 12.5,
        "pm2_5": 7.3,
        "co": 0.8,
        "no2": 15.0,
        "so2": 5.0,
        "ozone": 30.2
    }
    response = client.post("/api/data", json=payload)
    assert response.status_code == 201


def test_api_data_get_no_data(client) -> None:
    app = setup()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        dt = datetime.utcnow().isoformat()
        response = test_client.get(f"/api/data?datetime={dt}")
        assert response.status_code == 404