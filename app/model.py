from pydantic import BaseModel, Field, field_validator
from datetime import datetime


class AirQualityDataValidation(BaseModel):
    timestamp: datetime
    pm10: float = Field(..., ge=0, le=1000)
    pm2_5: float = Field(..., ge=0, le=1000)
    co: float = Field(..., ge=0, le=50)
    no2: float = Field(..., ge=0)
    so2: float = Field(..., ge=0)
    ozone: float = Field(..., ge=0)

    @field_validator("timestamp", mode="before")
    @classmethod
    def validate_timestamp(cls, value):
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                raise ValueError
        return value
