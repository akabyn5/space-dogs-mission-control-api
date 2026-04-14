from flask import Flask, jsonify, request
import requests
import os
import random

app = Flask(__name__)

API_KEY = os.getenv("OPENWEATHER_KEY")

@app.route("/status")
def status():
    return jsonify({
        "status": "ok",
        "service": "Space Dogs Mission Control API"
    })

@app.route("/status/detailed")
def detailed_status():
    return jsonify({
        "api_status": "running",
        "weather_api": "connected" if API_KEY else "not_configured"
    })

@app.route("/weather/launch-risk")
def launch_risk():
    city = request.args.get("city", "Panama")

    data, error = get_weather_data(city)

    if error:
        return jsonify(error), 500

    temp = data["main"]["temp"]
    wind = data["wind"]["speed"]

    if wind > 20:
        risk = "high"
    elif wind > 10:
        risk = "medium"
    else:
        risk = "low"

    return jsonify({
        "city": city,
        "temperature": temp,
        "wind_speed": wind,
        "launch_risk": risk
    })

@app.route("/launch-decision")
def decision():
    city = request.args.get("city", "Panama")

    data, error = get_weather_data(city)

    if error:
        return jsonify(error), 500

    wind = data["wind"]["speed"]

    if wind > 20:
        decision = "NO GO"
    else:
        decision = "GO"

    return jsonify({
        "city": city,
        "decision": decision
    })

@app.route("/mission/status")
def mission_status():
    return jsonify({
        "mission": "Space Dogs Test Mission",
        "weather_endpoint": "/weather/launch-risk",
        "decision_endpoint": "/launch-decision",
        "status": "READY"
    })

@app.route("/telemetry/simulated")
def telemetry():
    return jsonify({
        "altitude": random.randint(100, 400),
        "velocity": random.randint(7000, 8000),
        "status": "nominal"
    })

def get_weather_data(city):
    if not API_KEY:
        return None, {"error": "API key not configured"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        return None, {
            "error": "Request failed",
            "details": str(e)
        }

    if response.status_code != 200 or "main" not in data:
        return None, {
            "error": "Failed to fetch weather data",
            "details": data
        }

    return data, None


if __name__ == "__main__":
    app.run(debug=True)

