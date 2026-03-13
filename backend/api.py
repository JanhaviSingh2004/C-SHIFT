from flask import Flask, jsonify
from flask_cors import CORS

from backend.carbon_api import get_carbon_intensity
from backend.scheduler import get_container_status

API_KEY = "EwDxzHQuhmGJYDz46Xys"

app = Flask(__name__)
CORS(app)

@app.route("/status")
def status():

    carbon = get_carbon_intensity(API_KEY)

    running, stopped = get_container_status()

    return jsonify({
        "carbon_intensity": carbon,
        "running_containers": running,
        "stopped_containers": stopped
    })

if __name__ == "__main__":
    app.run()
