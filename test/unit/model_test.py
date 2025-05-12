import pytest
from app.model import AirQualityDataValidation
from datetime import datetime


def test_valid_reading():
    data = {
        "timestamp": "2024-05-01T12:00:00",
        "pm10": 20,
        "pm2_5": 10,
        "co": 0.5,
        "no2": 15,
        "so2": 3,
        "ozone": 25,
    }
    reading = AirQualityDataValidation.model_validate(data)
    assert reading.pm10 == 20
    assert isinstance(reading.timestamp, datetime)


def test_invalid_pm10():
    data = {
        "timestamp": "2024-05-01T12:00:00",
        "pm10": -5,
        "pm2_5": 10,
        "co": 0.5,
        "no2": 15,
        "so2": 3,
        "ozone": 25,
    }
    with pytest.raises(Exception):
        AirQualityDataValidation.model_validate(data)


def test_invalid_pm2_5():
    data = {
        "timestamp": "2024-05-01T12:00:00",
        "pm10": 10,
        "pm2_5": 100000,
        "co": 0.5,
        "no2": 15,
        "so2": 3,
        "ozone": 25,
    }
    with pytest.raises(Exception):
        AirQualityDataValidation.model_validate(data)


def test_invalid_co():
    data = {
        "timestamp": "2024-05-01T12:00:00",
        "pm10": 5,
        "pm2_5": 10,
        "co": -10,
        "no2": 15,
        "so2": 3,
        "ozone": 25,
    }
    with pytest.raises(Exception):
        AirQualityDataValidation.model_validate(data)


def test_invalid_no2():
    data = {
        "timestamp": "2024-05-01T12:00:00",
        "pm10": 5,
        "pm2_5": 10,
        "co": 0.5,
        "no2": -10,
        "so2": 3,
        "ozone": 25,
    }
    with pytest.raises(Exception):
        AirQualityDataValidation.model_validate(data)


def test_invalid_so2():
    data = {
        "timestamp": "2024-05-01T12:00:00",
        "pm10": 5,
        "pm2_5": 10,
        "co": 0.5,
        "no2": 15,
        "so2": -10,
        "ozone": 25,
    }
    with pytest.raises(Exception):
        AirQualityDataValidation.model_validate(data)


def test_invalid_ozone():
    data = {
        "timestamp": "2024-05-01T12:00:00",
        "pm10": -5,
        "pm2_5": 10,
        "co": 0.5,
        "no2": 15,
        "so2": 3,
        "ozone": -2137,
    }
    with pytest.raises(Exception):
        AirQualityDataValidation.model_validate(data)


def test_invalid_timestamp():
    data = {
        "timestamp": "TechniSchools",
        "pm10": -5,
        "pm2_5": 10,
        "co": 0.5,
        "no2": 15,
        "so2": 3,
        "ozone": -2137,
    }
    with pytest.raises(Exception):
        AirQualityDataValidation.model_validate(data)
