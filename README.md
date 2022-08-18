# XSS-Cookie-Hijacker

Hijack Cookies by exploting XSS vulnerable applications or use it to dump and retreive data over the internet

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
