from flask import Flask
from app.controller import DataAPI


def setup():
    app = Flask(__name__)
    app.add_url_rule("/api/data", view_func=DataAPI.as_view("data_api"))
    return app


if __name__ == "__main__":
    app = setup()
    app.run()
