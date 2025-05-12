from datetime import datetime
from app.model import AirQualityReading


class AirQualityService:
    def __init__(self, repository):
        self.repository = repository

    def save_reading(self, data: dict):
        reading = AirQualityReading.model_validate(data)
        self.repository.add(reading)
        return reading

    def get_closest_reading(self, dt_str: str):
        dt = datetime.fromisoformat(dt_str)
        return self.repository.find_closest(dt)