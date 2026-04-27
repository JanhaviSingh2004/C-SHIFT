from flask import Flask, jsonify
from flask_cors import CORS
import docker

from backend.carbon_api import get_carbon_intensity

API_KEY = "EwDxzHQuhmGJYDz46Xys"

app = Flask(__name__)
CORS(app)

# Docker client
client = docker.from_env()

# ✅ ADD THIS FUNCTION
def get_container_status():
    containers = client.containers.list(all=True)

    running = []
    stopped = []

    for c in containers:
        if c.status == "running":
            running.append(c.name)
        else:
            stopped.append(c.name)

    return running, stopped


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
    app.run(debug=True)