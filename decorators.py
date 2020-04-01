from time import perf_counter

def timer(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print(f'Time taken: \t {duration:2f}')
        return result
    return inner

