import pytest

from weerman.coordinates import get_city_coordinates


def test_get_coordinates_of_valid_city():
    city = "Владивосток"
    coordinates = get_city_coordinates(city)

    assert round(coordinates.latitude, 3) == 43.115
    assert round(coordinates.longitude, 3) == 131.886


def test_get_coordinates_of_invalid_city():
    city = "Такого города не существует"

    with pytest.raises(ValueError):
        get_city_coordinates(city)


def test_get_coordinates_with_no_city():
    with pytest.raises(ValueError):
        get_city_coordinates(None)
