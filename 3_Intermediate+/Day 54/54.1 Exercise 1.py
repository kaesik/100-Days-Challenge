import time

current_time = time.time()

def speed_calc_decorator(function):
    function()
    end_time = time.time()
    print(f"Time taken: {end_time - current_time}")

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

try:
    fast_function()
    slow_function()
except:
    pass