import random
import time
from functools import lru_cache


@lru_cache(maxsize=100)
def get_data(user_id):
    return perform_expensive_operation(user_id)


def perform_expensive_operation(user_id):
    # Simulating a delay to mimic the time taken to query a database
    time.sleep(random.uniform(0.5, 2.0))

    # Mock user data typically fetched from a database
    user_data = {
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"},
        3: {"name": "Charlie", "email": "charlie@example.com"},
    }

    # Retrieve user details based on user_id
    result = user_data.get(user_id, {"error": "User not found"})

    return result


if __name__ == "__main__":
    print(get_data(1))
    print(get_data(1))
    print(get_data(2))
    print(get_data(99))
