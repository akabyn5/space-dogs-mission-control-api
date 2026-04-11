from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/weather")
def status():
    return jsonify({
        "temperature": 30,
        "wind_speed": 12,
        "launch_risk": "medium"
    })

if __name__ == "__main__":
    app.run(debug=True)