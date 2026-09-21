import time
import functools

def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.f} seconds.")
        return result
    return wrapper

@measure_time
def calculate_sum(n):
    if n < 0:
        return 0
    return sum(range(0, n + 1))

print(calculate_sum(1000000))

