import pytest

from weerman.app import app as weerman_app


@pytest.fixture
def app():
    yield weerman_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_weather_with_valid_city(client):
    response = client.get("/weather?city=Владивосток")
    assert response.status_code == 200

    weather = response.get_json()
    assert set(weather.keys()) == set(
        [
            "condition",
            "temperature",
            "minimum_temperature",
            "maximum_temperature",
            "feels_like",
            "pressure",
            "humidity",
            "visibility",
            "wind_speed",
        ]
    )


def test_weather_with_no_city(client):
    response = client.get("/weather")
    assert response.status_code == 400
