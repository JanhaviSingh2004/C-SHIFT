import os

def start_container(container_name):
    print(f"Starting container: {container_name}")
    os.system(f"docker start {container_name}")

def stop_container(container_name):
    print(f"Stopping container: {container_name}")
    os.system(f"docker stop {container_name}")

def restart_container(container_name):
    print(f"Restarting container: {container_name}")
    os.system(f"docker restart {container_name}")
if __name__ == "__main__":
    stop_container("ml-training")