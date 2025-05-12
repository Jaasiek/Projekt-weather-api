from app.model import AirQualityDataValidation
from app.repository import AirQualityRepo
from datetime import datetime


def test_add_and_find_closest() -> None :
    repo = AirQualityRepo()
    reading1 = AirQualityDataValidation(timestamp="2024-05-01T12:00:00", pm10=10, pm2_5=5, co=0.4, no2=15, so2=2, ozone=30)
    reading2 = AirQualityDataValidation(timestamp="2024-05-01T15:00:00", pm10=12, pm2_5=6, co=0.6, no2=17, so2=3, ozone=32)

    repo.add(reading1)
    repo.add(reading2)

    target_time = datetime.fromisoformat("2024-05-01T13:00:00")
    closest = repo.find_closest(target_time)

    assert closest.timestamp == reading1.timestamp
