from flask import Flask
from app.controller import DataAPI
import client


app = Flask(__name__)
app.add_url_rule("/api/data", view_func=DataAPI.as_view("data_api"))

if __name__ == "__main__":
    app.run()
    client.main("Warsaw")
