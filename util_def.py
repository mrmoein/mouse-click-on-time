import datetime
import threading
import time
from pynput.mouse import Controller, Button

mouse = Controller()


def start_clicking(after_click):
    print("Function called at:", datetime.datetime.now().strftime("%H:%M:%S.%f"))

    for millisecond_time in after_click:
        t0 = time.time()
        mouse.click(Button.left)
        t1 = time.time()
        time.sleep(millisecond_time - (t1 - t0))

    mouse.click(Button.left)


def is_time_passed(target_time):
    if datetime.datetime.now() >= target_time:
        return True
    return False


def call_function_on_exact_time(time_string, after_click):
    scheduled_time = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S.%f")

    if is_time_passed(scheduled_time):
        print("time passed! check time")
        exit()

    while True:
        if is_time_passed(scheduled_time):
            time_difference = (datetime.datetime.now() - scheduled_time).total_seconds() * 1000
            if 0 <= time_difference:
                start_clicking(after_click)
                break
        else:
            time.sleep(0.001)
