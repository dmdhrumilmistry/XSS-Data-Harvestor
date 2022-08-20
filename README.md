# XSS-Data-Harvestor

Harvest data from XSS vulnerabilites to XSS-Data-Harvestor API

Example: Hijack Cookies by exploting XSS vulnerable applications to dump and retreive data over the internet using ssh tunelling or on hosted platform.

## Installation

- Install [Python](https://python.org/)

- Install requirements

  ```bash
  python -m pip install -r requirements.txt
  ```

## Start Applications

- using flask

  ```bash
  python app.py # debug mode
  ```

- Using gunicorn wsgi

  ```bash
  gunicorn wsgi:app --bind 0.0.0.0:5000
  ```

## Endpoints

|       Endpoint       |  Methods  | Description                                                        |
| :------------------: | :-------: | :----------------------------------------------------------------- |
|        /api/         |    \*     | API home                                                           |
|     /api/hacked      | GET, POST | accepts hacked data in json/form data format or from url parameter |
| /api/get_hacked_data |    GET    | returns hacked data in json format                                 |
