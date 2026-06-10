from flask import Flask, jsonify
from flask_cors import CORS
import os

from backend.carbon_api import get_carbon_intensity

API_KEY = "EwDxzHQuhmGJYDz46Xys"

app = Flask(__name__)
CORS(app)


@app.route("/status")
def status():

    carbon = get_carbon_intensity(API_KEY)

    if carbon and carbon > 600:
        running = ["analytics-job"]
        stopped = ["ml-training", "backup-job"]
    else:
        running = ["analytics-job", "ml-training", "backup-job"]
        stopped = []

    return jsonify({
        "carbon_intensity": carbon,
        "running_containers": running,
        "stopped_containers": stopped
    })


@app.route("/")
def home():
    return jsonify({"message": "C-Shift API Running"})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )