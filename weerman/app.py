from flask import Flask, request, abort

from requests import RequestException

from .coordinates import get_city_coordinates
from .weather import get_weather_by_coordinates

app = Flask(__name__)


@app.route("/weather")
def weather():
    try:
        city = request.args["city"]
    except KeyError:
        abort(400)

    try:
        coordinates = get_city_coordinates(city)
    except ValueError:
        abort(404)

    try:
        weather = get_weather_by_coordinates(coordinates)
    except RequestException:
        abort(500)

    return weather._asdict()
