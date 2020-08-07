from collections import namedtuple
from functools import partial

from geopy.geocoders import Nominatim

Coordinates = namedtuple("Coordinates", ["latitude", "longitude"])


def get_city_coordinates(city: str) -> Coordinates:
    if city is None:
        raise ValueError("City must be provided.")

    geolocator = Nominatim(user_agent="weerman")
    geocode = partial(geolocator.geocode, language="ru")
    location = geocode(city)
    if location is None:
        raise ValueError("City does not exist.")

    return Coordinates(latitude=location.latitude, longitude=location.longitude)
