import main
import schedule
import time

def call_event():
    main.check_todays_bd("Birthday.csv")

if __name__ == '__main__':
    schedule.every(10).seconds.do(call_event)
    # schedule.every(24).hour.do(call_event)
    while True:
        schedule.run_pending()
        time.sleep(10)