import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])

API_KEY = "8984301b884d6539a535d85e24906e99"

def get_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        forecasts = []

        daily_forecast = {}
        for forecast in data["list"]:
            date = forecast["dt_txt"].split(" ")[0]
            temp_min = forecast["main"]["temp_min"]
            temp_max = forecast["main"]["temp_max"]
            condition = forecast["weather"][0]["description"]

            if date not in daily_forecast:
                daily_forecast[date] = {
                    "temp_min": temp_min,
                    "temp_max": temp_max,
                    "condition": condition
                }
            else:
                daily_forecast[date]["temp_min"] = min(daily_forecast[date]["temp_min"], temp_min)
                daily_forecast[date]["temp_max"] = max(daily_forecast[date]["temp_max"], temp_max)

            if len(daily_forecast) == 4:
                break

        forecasts = [{"date": date, **info} for date, info in daily_forecast.items()]
        return forecasts
    elif response.status_code == 404:
        return {"error": f"No se encontró información del clima para la ciudad: {city}"}, 404
    else:
        return {"error": "Error al conectarse al servicio de clima"}, response.status_code

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Por favor, proporciona el nombre de una ciudad en el parámetro 'city'"}), 400

    forecast = get_weather_forecast(city)
    return jsonify(forecast)

if __name__ == "__main__":
    app.run(debug=True)
