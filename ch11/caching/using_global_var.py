import time
import random

# Global variable as cache
_cache = {}


def get_data(query):
    if query in _cache:
        return _cache[query]  # Return cached result
    else:
        result = perform_expensive_operation(query)
        _cache[query] = result
        return result


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
