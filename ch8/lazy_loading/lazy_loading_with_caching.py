import time
from functools import lru_cache


def recursive_factorial(n):
    """Calculate factorial (expensive for large n)"""
    if n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


@lru_cache(maxsize=128)
def cached_factorial(n):
    return recursive_factorial(n)


def main():
    # Testing the performance

    n = 20

    # Without caching
    start_time = time.time()
    print(f"Recursive factorial of {n}: {recursive_factorial(n)}")
    print(f"Calculation time without caching: {time.time() - start_time} seconds.")

    # With caching
    start_time = time.time()
    print(f"Cached factorial of {n}: {cached_factorial(n)}")
    print(f"Calculation time with caching: {time.time() - start_time} seconds.")

    print(f"Cache statistics:\n  {cached_factorial.cache_info()}")


if __name__ == "__main__":
    main()
