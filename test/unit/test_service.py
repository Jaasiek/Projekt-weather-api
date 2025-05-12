import pytest
from app.service import AirQualityService
from app.repository import AirQualityRepo


def test_save_and_get_reading() -> None:
    repo = AirQualityRepo()
    service = AirQualityService(repo)

    data = {
        "timestamp": "2024-05-01T10:00:00",
        "pm10": 20,
        "pm2_5": 8,
        "co": 0.5,
        "no2": 13,
        "so2": 2,
        "ozone": 40,
    }

    saved = service.save_reading(data)
    assert saved.pm10 == 20

    result = service.get_closest_reading("2024-05-01T10:30:00")
    assert result.timestamp == saved.timestamp


def test_service_invalid_data() -> None:
    repo = AirQualityRepo()
    service = AirQualityService(repo)

    data = {
        "timestamp": "2024-05-01T10:00:00",
        "pm10": -10,
        "pm2_5": 8,
        "co": 0.5,
        "no2": 13,
        "so2": 2,
        "ozone": 40,
    }

    with pytest.raises(Exception):
        service.save_reading(data)
