from flask import Flask, jsonify, request
import requests
import os

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

    if not API_KEY:
        return jsonify({
            "error": "API key not configured"
        }), 500

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        return jsonify({
            "error": "Request failed",
            "details": str(e)
        }), 500

    if response.status_code != 200 or "main" not in data:
        return jsonify({
            "error": "Failed to fetch weather data",
            "details": data
        }), 500

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

if __name__ == "__main__":
    app.run(debug=True)