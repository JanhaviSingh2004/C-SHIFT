from backend.carbon_api import get_carbon_intensity
from backend.container_manager import start_container, stop_container
from config.settings import CARBON_THRESHOLD, WORKLOADS


def run_scheduler(api_key):

    carbon = get_carbon_intensity(api_key)

    if carbon is None:
        print("Could not fetch carbon intensity")
        return

    print("Current Carbon Intensity:", carbon)

    if carbon > CARBON_THRESHOLD:

        print("⚠ High carbon → stopping HEAVY workloads")

        # stop only heavy
        for c in WORKLOADS["heavy"]:
            stop_container(c)

        # medium optional (only if very high)
        if carbon > 600:
            print("🔥 Very high carbon → stopping MEDIUM workloads")
            for c in WORKLOADS["medium"]:
                stop_container(c)

        # critical ALWAYS running
        for c in WORKLOADS["critical"]:
            start_container(c)

    else:

        print("✅ Low carbon → running all workloads")

        # start everything
        for category in WORKLOADS:
            for c in WORKLOADS[category]:
                start_container(c)