from flask import Flask, request

from requests import RequestException

from .coordinates import get_city_coordinates
from .weather import get_weather_by_coordinates

app = Flask(__name__)


@app.route("/current-weather", methods=["GET"])
def current_weather():
    try:
        city = request.args["city"]
    except KeyError:
        return {"error": "City must be specified."}, 400

    try:
        coordinates = get_city_coordinates(city)
    except ValueError:
        return {"error": "City does not exist."}, 404

    try:
        weather = get_weather_by_coordinates(coordinates)
    except RequestException:
        return {"error": "Something went wrong."}, 500

    return weather._asdict()
