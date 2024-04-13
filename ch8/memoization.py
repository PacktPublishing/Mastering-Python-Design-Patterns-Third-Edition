from datetime import timedelta
from functools import lru_cache


def fibonacci_func1(n):
    if n < 2:
        return n
    return fibonacci_func1(n - 1) + fibonacci_func1(n - 2)


@lru_cache(maxsize=None)
def fibonacci_func2(n):
    if n < 2:
        return n
    return fibonacci_func2(n - 1) + fibonacci_func2(n - 2)


def main():
    import time

    n = 30

    start_time = time.time()
    result = fibonacci_func1(n)
    duration = timedelta(time.time() - start_time)
    print(f"Fibonacci_func1({n}) = {result}, calculated in {duration}")

    start_time = time.time()
    result = fibonacci_func2(n)
    duration = timedelta(time.time() - start_time)
    print(f"Fibonacci_func2({n}) = {result}, calculated in {duration}")


if __name__ == "__main__":
    main()
