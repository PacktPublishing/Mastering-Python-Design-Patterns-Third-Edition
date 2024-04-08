from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    import time

    n = 30  # Test with a relatively large value to illustrate the benefit
    start_time = time.time()
    result = fibonacci(n)
    duration = time.time() - start_time
    print(f"Fibonacci({n}) = {result}, calculated in {duration} seconds")


if __name__ == "__main__":
    main()
