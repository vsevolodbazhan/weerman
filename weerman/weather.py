import os
from collections import namedtuple
from typing import Any, Dict

from requests import get

from .coordinates import Coordinates

Weather = namedtuple(
    "Weather",
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
    ],
)


def get_weather_by_coordinates(coordinates: Coordinates) -> Weather:
    parameters = {
        "lat": coordinates.latitude,
        "lon": coordinates.longitude,
        "appid": os.environ["OPEN_WEATHER_API_KEY"],
        "lang": "ru",
        "units": "metric",
    }
    url = build_request_url(parameters)

    response = get(url)
    response.raise_for_status()

    parameters = response.json()
    return parse_weather_response_parameters(parameters)


def build_request_url(parameters: Dict[str, Any]) -> str:
    if "appid" not in parameters:
        raise AttributeError("`appid` is a required parameter.")

    url = "https://api.openweathermap.org/data/2.5/weather"
    query_parameters = "&".join(f"{key}={value}" for key, value in parameters.items())
    return f"{url}?{query_parameters}"


def parse_weather_response_parameters(parameters: Dict[str, Any]) -> Weather:
    weather = parameters["weather"][0]
    main = parameters["main"]
    visibility = parameters["visibility"]
    wind = parameters["wind"]

    return Weather(
        condition=weather["description"].capitalize(),
        temperature=main["temp"],
        minimum_temperature=main["temp_min"],
        maximum_temperature=main["temp_max"],
        feels_like=main["feels_like"],
        pressure=main["pressure"],
        humidity=main["humidity"],
        visibility=visibility,
        wind_speed=wind["speed"],
    )
