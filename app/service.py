from datetime import datetime
from app.model import AirQualityDataValidation


class AirQualityService:
    def __init__(self, repository):
        self.repository = repository

    def save_reading(self, data: dict):
        reading = AirQualityDataValidation.model_validate(data)
        self.repository.add(reading)
        return reading

    def get_closest_reading(self, dt_str: str):
        dt = datetime.fromisoformat(dt_str)
        return self.repository.find_closest(dt)