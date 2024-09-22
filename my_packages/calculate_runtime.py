import time


def calculate_func_runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"函数 {func.__name__} 花了 {end_time - start_time:.6f} 秒.")
        return result

    return wrapper
