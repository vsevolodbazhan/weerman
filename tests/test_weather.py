import json

import httpretty
import pytest

from weerman.coordinates import Coordinates
from weerman.weather import (
    build_request_url,
    get_weather_by_coordinates,
    parse_weather_response_parameters,
)

RESPONSE_EXAMPLE = {
    "coord": {"lon": 131.89, "lat": 43.12},
    "weather": [{"id": 800, "main": "Clear", "description": "ясно", "icon": "01n"}],
    "base": "stations",
    "main": {
        "temp": 18,
        "feels_like": 18.92,
        "temp_min": 18,
        "temp_max": 18,
        "pressure": 1009,
        "humidity": 93,
    },
    "visibility": 10000,
    "wind": {"speed": 2, "deg": 310},
    "clouds": {"all": 0},
    "dt": 1596809622,
    "sys": {
        "type": 1,
        "id": 8885,
        "country": "RU",
        "sunrise": 1596831024,
        "sunset": 1596882350,
    },
    "timezone": 36000,
    "id": 2013348,
    "name": "Владивосток",
    "cod": 200,
}


def test_build_request_url_without_parameters():
    with pytest.raises(AttributeError):
        build_request_url(parameters={})


def test_build_request_url_without_appid():
    parameters = {"lon": 131.89, "lat": 43.12}

    with pytest.raises(AttributeError):
        build_request_url(parameters=parameters)


def test_build_request_url_with_valid_parameters():
    parameters = {"lon": 131.89, "lat": 43.12, "appid": "787adad"}
    url = build_request_url(parameters=parameters)

    url_without_parameters = "https://api.openweathermap.org/data/2.5/weather"
    assert url == f"{url_without_parameters}?lon=131.89&lat=43.12&appid=787adad"


def test_parse_valid_weather_response_parameters():
    parameters = RESPONSE_EXAMPLE
    weather = parse_weather_response_parameters(parameters)

    assert weather.condition == "Ясно"
    assert weather.temperature == 18
    assert weather.minimum_temperature == 18
    assert weather.maximum_temperature == 18
    assert weather.feels_like == 18.92
    assert weather.pressure == 1009
    assert weather.humidity == 93
    assert weather.visibility == 10000
    assert weather.wind_speed == 2


@httpretty.activate
def test_get_weather_by_coordinates():
    url_without_parameters = "https://api.openweathermap.org/data/2.5/weather"
    url = f"{url_without_parameters}?lon=131.89&lat=43.12&appid=787adad"
    httpretty.register_uri(
        httpretty.GET,
        url,
        body=json.dumps(RESPONSE_EXAMPLE),
        status=200,
        content_type="text/json",
    )

    weather = get_weather_by_coordinates(Coordinates(131.89, 43.12))

    assert weather.condition == "Ясно"
    assert weather.temperature == 18
    assert weather.minimum_temperature == 18
    assert weather.maximum_temperature == 18
    assert weather.feels_like == 18.92
    assert weather.pressure == 1009
    assert weather.humidity == 93
    assert weather.visibility == 10000
    assert weather.wind_speed == 2
