import time

def speed_calc_decorator(function):
    def runtime():
        before_run = time.time()
        function()
        after_run = time.time()
        print(f"{function.__name__} run speed: {after_run - before_run}s")
    return runtime

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator  
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()