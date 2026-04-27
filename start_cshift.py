import os
import subprocess
import time
import sys

print("Starting C-Shift System...")

print("Starting Docker containers...")
os.system("docker start ml-training")
os.system("docker start backup-job")
os.system("docker start analytics-job")

time.sleep(2)

print("Starting Carbon Scheduler...")
subprocess.Popen([sys.executable, "run_scheduler.py"])

time.sleep(2)

print("Starting Backend API...")
subprocess.Popen([sys.executable, "-m", "backend.api"])

print("\nC-Shift is running!")
print("Open dashboard: frontend/index.html")