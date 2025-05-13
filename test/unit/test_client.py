import client


def test_get_coordinates() -> None:
    assert client.get_coordinates("Warsaw") == (52.22977, 21.01178)


def test_fetch_air_quality_data() -> None:
    assert client.fetch_air_quality_data(52.22977, 21.01178) != {}


def test_get_latest_reading() -> None:
    data = client.fetch_air_quality_data(52.22977, 21.01178)
    assert client.get_latest_reading(data) != {}


def test_send_to_backend() -> None:
    data = client.fetch_air_quality_data(52.22977, 21.01178)
    reading = client.get_latest_reading(data)
    assert client.send_to_backend(reading) == "success"
