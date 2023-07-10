import pyautogui
import datetime
import time

START_TIME = "03:56:15.507"
AFTER_CLICK = [0.500, 0.400, 0.444]


def my_function():
    print("Function called at", datetime.datetime.now())
    pyautogui.click()

    for millisecond_time in AFTER_CLICK:
        time.sleep(millisecond_time)
        pyautogui.click()


def call_function_on_exact_time(time_string):
    scheduled_time = datetime.datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S.%f")

    while True:
        current_time = datetime.datetime.now()

        if current_time >= scheduled_time:
            time_difference = (current_time - scheduled_time).total_seconds() * 1000
            if 0 <= time_difference < 1:
                my_function()
                break
        else:
            time.sleep(0.001)


call_function_on_exact_time("{} {}".format(datetime.datetime.now().strftime('%Y-%m-%d'), START_TIME))
