import os
import subprocess
import time


print("Starting C-Shift System...")


print("Starting Docker containers...")
os.system("docker start ml-training")
os.system("docker start backup-job")
os.system("docker start analytics-job")


time.sleep(2)


print("Starting Carbon Scheduler...")
subprocess.Popen(["python","run_scheduler.py"])


time.sleep(2)


print("Starting Backend API...")
subprocess.Popen(["python","-m","backend.api"])


print("\nC-Shift is running!")
print("Open dashboard: index.html")
