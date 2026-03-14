import time
from backend.scheduler import run_scheduler
from config.settings import CHECK_INTERVAL


API_KEY = "EwDxzHQuhmGJYDz46Xys"



def main():
    print("Starting C-Shift Carbon-Aware Scheduler...")


    while True:
        run_scheduler(API_KEY)
        time.sleep(CHECK_INTERVAL)



if __name__ == "__main__":
    main()