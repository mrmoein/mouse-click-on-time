import datetime
from util_def import call_function_on_exact_time

START_TIME = "06:10:15.537"
AFTER_CLICK = [0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400, 0.400]
#              -> -> -> -> -> ->

print('click at:', START_TIME)

target_time = f"{datetime.datetime.now().strftime('%Y-%m-%d')} {START_TIME}"

call_function_on_exact_time(target_time, AFTER_CLICK)
