from flask import Flask, request, abort

from .coordinates import get_city_coordinates
from .weather import get_weather_by_coordinates

app = Flask(__name__)


@app.route("/weather")
def weather():
    if "city" not in request.args:
        abort(400, "City must be specified.")

    city = request.args.get("city")
    coordinates = get_city_coordinates(city)
    weather = get_weather_by_coordinates(coordinates)

    return weather._asdict()
