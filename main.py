from datetime import datetime, time
from threading import Timer
from tg.bot import send_channel
from decide_lunch import getDecision
import os

time2decide = os.environ.get("MSG_TIME", '12:15')

def getTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def check_within_weekdays():
    return 1<=datetime.today().isoweekday()<=5

def check_time2decide():
    now = datetime.now()
    return now.strftime("%H:%M") == time2decide

def recur_check():
    # Decide and send message at {{time2decide}} in weekdays
    if check_time2decide() and check_within_weekdays():
       send_decision()

    # Repeat every minutes
    timer_interval_sec = 60
    t = Timer(timer_interval_sec, recur_check)
    t.start()

def send_decision():
    decision_today = getDecision()
    print(getTime(), decision_today)
    msg = f'投咩票啫?\n極權bot決定今日lunch食:\n<i><u><b>%s</b></u></i>' % decision_today
    send_channel(msg)

if __name__ == '__main__':
    
    print(getTime(), "Program Start!")
    print("The decision time on weekdays: ", time2decide)
    # send_channel("Program Start!")
    
    recur_check()
    # send_decision()