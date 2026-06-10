from flask import Flask, jsonify
from flask_cors import CORS

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


if __name__ == "__main__":
    app.run(debug=True)