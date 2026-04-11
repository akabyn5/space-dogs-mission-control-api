from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/weather")
def weather():
    data = {
        "temperature": 30,
        "wind_speed": 12
        }
    if data["wind_speed"] > 20:
        risk = "high"
    elif data["wind_speed"] > 10:
        risk = "medium"
    else:
        risk = "low"
        data["launch_risk"] = risk
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)