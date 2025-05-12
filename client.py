import requests

BACKEND_URL = "http://localhost:5000/api/data"


def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if not data.get("results"):
        raise ValueError(f"Invalid city name {city}")
    result = data["results"][0]
    return result["latitude"], result["longitude"]


def fetch_air_quality_data(lat, lon):
    url = (
        f"https://air-quality-api.open-meteo.com/v1/air-quality?"
        f"latitude={lat}&longitude={lon}&hourly=pm10,pm2_5,carbon_monoxide,"
        f"nitrogen_dioxide,sulphur_dioxide,ozone"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_latest_reading(data):
    idx = -1
    timestamps = data["hourly"]["time"]
    return {
        "timestamp": timestamps[idx],
        "pm10": data["hourly"]["pm10"][idx],
        "pm2_5": data["hourly"]["pm2_5"][idx],
        "co": data["hourly"]["carbon_monoxide"][idx],
        "no2": data["hourly"]["nitrogen_dioxide"][idx],
        "so2": data["hourly"]["sulphur_dioxide"][idx],
        "ozone": data["hourly"]["ozone"][idx],
    }


def send_to_backend(reading):
    response = requests.post(BACKEND_URL, json=reading)
    if response.status_code == 201:
        print("Data correctly send to backend")
    else:
        print(f"An error occurred{response.status_code}, {response.text}")


def main(city):
    try:
        lat, lon = get_coordinates(city)
        data = fetch_air_quality_data(lat, lon)
        reading = get_latest_reading(data)
        send_to_backend(reading)
    except Exception as e:
        print("An error occurred", e)
