import docker
from backend.carbon_api import get_carbon_intensity
from backend.container_manager import start_container, stop_container
from config.settings import CARBON_THRESHOLD, WORKLOADS


client = docker.from_env()


def run_scheduler(api_key):

    carbon = get_carbon_intensity(api_key)

    if carbon is None:
        print("Could not fetch carbon intensity")
        return

    print("Current Carbon Intensity:", carbon)

    # Decision Logic
    if carbon > CARBON_THRESHOLD:

        print("High carbon detected → pausing heavy workloads")

        stop_container(WORKLOADS["ml_training"])
        stop_container(WORKLOADS["backup_job"])
        stop_container(WORKLOADS["analytics_job"])

    else:

        print("Carbon level acceptable → running workloads")

        start_container(WORKLOADS["ml_training"])
        start_container(WORKLOADS["backup_job"])
        start_container(WORKLOADS["analytics_job"])


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