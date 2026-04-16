from flask import Flask, jsonify, request
import requests
import os
import random
from flask_cors import CORS          # ← importa CORS

app = Flask(__name__)
CORS(app)                            # ← activa CORS para toda la app

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

def get_weather_data(city):
    if not API_KEY:
        return None, {"error": "API key not configured"}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        return None, {
            "error": "Request failed",
            "details": str(e)
        }

    if "main" not in data or "wind" not in data:
        return None, {
            "error": "Failed to fetch weather data",
            "details": data
        }

    return data, None

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

    decision = "NO GO" if wind > 20 else "GO"

    return jsonify({
        "city": city,
        "decision": decision
    })

@app.route("/telemetry/simulated")
def telemetry():
    return jsonify({
        "altitude": random.randint(100, 400),
        "velocity": random.randint(7000, 8000),
        "status": "nominal"
    })

@app.route("/ai/mission-advice")
def mission_advice():
    city = request.args.get("city", "Panama")

    data, error = get_weather_data(city)

    if error:
        return jsonify({
            "city": city,
            "advice": "Weather data unavailable. Cannot assess launch conditions.",
            "temperature": None,
            "wind_speed": None
            }), 500

    wind = data["wind"]["speed"]
    temp = data["main"]["temp"]

    if wind > 20:
        advice = "Conditions are unsafe. High wind speeds detected. Launch is not recommended."
    elif wind > 10:
        advice = "Moderate risk. Evaluate carefully before launch."
    else:
        advice = "Conditions are favorable. Launch can proceed."

    return jsonify({
        "city": city,
        "advice": advice,
        "temperature": temp,
        "wind_speed": wind
    })

@app.route("/mission/status")
def mission_status():
    return jsonify({
        "mission": "Space Dogs Test Mission",
        "weather_endpoint": "/weather/launch-risk",
        "decision_endpoint": "/launch-decision",
        "telemetry_endpoint": "/telemetry/simulated",
        "ai_endpoint": "/ai/mission-advice",
        "status": "READY"
    })

if __name__ == "__main__":
    app.run(debug=True)