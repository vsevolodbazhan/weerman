# Weerman

[![Build Status](https://travis-ci.com/vsevolodbazhan/weerman.svg?branch=master)](https://travis-ci.com/vsevolodbazhan/weerman)
[![CodeFactor](https://www.codefactor.io/repository/github/vsevolodbazhan/weerman/badge)](https://www.codefactor.io/repository/github/vsevolodbazhan/weerman)
[![codecov](https://codecov.io/gh/vsevolodbazhan/weerman/branch/master/graph/badge.svg)](https://codecov.io/gh/vsevolodbazhan/weerman)

Weather forecast microservice for [Tomoru](https://app.tomoru.ru/).

## Installation

Install dependencies using [pip](https://pip.pypa.io/en/stable/):

```
pip install -r requirements.txt
```

or [Poetry](https://python-poetry.org):

```
poetry install
```

Poetry will install dev-dependencies as well. So use that if you are planning to contribute.

## Usage

Run using [Gunicorn](https://gunicorn.org):

```
gunicorn weerman.app:app
```

Go ahead and make a request:

```
http GET http://127.0.0.1:8000/current-weather city==Vladivostok
```

You should get this response:

```
HTTP/1.1 200 OK
Connection: close
Content-Length: 271
Content-Type: application/json
Date: Sat, 08 Aug 2020 03:10:27 GMT
Server: gunicorn/20.0.4

{
    "condition": "Облачно с прояснениями",
    "feels_like": 22.95,
    "humidity": 73,
    "maximum_temperature": 22,
    "minimum_temperature": 22,
    "pressure": 756.0,
    "temperature": 22,
    "wind_speed": 2
}
```

I have used [HTTPie](https://httpie.org) for this example.

## License

[MIT](https://github.com/vsevolodbazhan/weerman/blob/master/LICENSE)
