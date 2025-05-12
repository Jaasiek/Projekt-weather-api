import pytest
from main import setup
from datetime import datetime, timedelta
import json


@pytest.fixture
def client():
    app = setup()
    app.testing = True
    return app.test_client()


def test_post_valid_data(client):
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "pm10": 30,
        "pm2_5": 15,
        "co": 0.6,
        "no2": 14,
        "so2": 3,
        "ozone": 22,
    }
    response = client.post("/api/data", json=data)
    assert response.status_code == 201
    res_json = response.get_json()
    assert res_json["data"]["pm10"] == 30


def test_post_invalid_data(client):
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "pm10": -50,
        "pm2_5": 15,
        "co": 0.6,
        "no2": 14,
        "so2": 3,
        "ozone": 22,
    }
    response = client.post("/api/data", json=data)
    assert response.status_code == 400


def test_get_closest_reading(client):
    ts = datetime.utcnow().replace(microsecond=0)
    data = {
        "timestamp": ts.isoformat(),
        "pm10": 42,
        "pm2_5": 18,
        "co": 0.3,
        "no2": 20,
        "so2": 2,
        "ozone": 33,
    }
    client.post("/api/data", json=data)

    response = client.get(f"/api/data?datetime={ts.isoformat()}")
    assert response.status_code == 200
    result = response.get_json()
    assert result["pm10"] == 42
