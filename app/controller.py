from flask.views import MethodView
from flask import request, jsonify
from app.repository import AirQualityRepo
from app.service import AirQualityService

repo = AirQualityRepo()
service = AirQualityService(repo)


class DataAPI(MethodView):
    def post(self):
        try:
            data = request.get_json()
            reading = service.save_reading(data)
            return jsonify({"status": "success", "data": reading.model_dump()}), 201
        except Exception as e:
            return jsonify({"An error occurred": str(e)}), 400

    def get(self):
        datetime_str = request.args.get("datetime")
        if not datetime_str:
            return jsonify({"An error occurred": "Missing 'datetime' query parameter"}), 400
        try:
            reading = service.get_closest_reading(datetime_str)
            if reading:
                return jsonify(reading.model_dump())
            else:
                return jsonify({"An error occurred": "No data available"}), 404
        except Exception as e:
            return jsonify({"An error occurred": str(e)}), 400
