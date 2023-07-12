import datetime
import threading
import time
from pynput.mouse import Controller, Button

mouse = Controller()

# event = threading.Event()


def start_clicking(after_click):
    print("Function called at:", datetime.datetime.now().strftime("%H:%M:%S.%f"))

    for millisecond_time in after_click:
        t0 = time.time()
        mouse.click(Button.left)
        t1 = time.time()
        # event.wait(millisecond_time - (t1 - t0))
        time.sleep(millisecond_time - (t1 - t0))

    mouse.click(Button.left)


def is_time_passed(target_time):
    if datetime.datetime.now() >= target_time:
        return True
    return False


def call_function_on_exact_time(time_string, after_click):
    scheduled_time = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S.%f")

    current_time = datetime.datetime.now()

    time_difference = (scheduled_time - current_time).total_seconds()

    if time_difference <= 0:
        print("time passed! check time")
        exit()

    time.sleep(time_difference)
    # event.wait(time_difference)
    start_clicking(after_click)

