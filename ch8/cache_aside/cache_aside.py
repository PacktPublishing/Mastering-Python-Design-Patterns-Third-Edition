import sqlite3
import sys
from pathlib import Path

import redis

CACHE_KEY_PREFIX = "quote"
DB_PATH = Path(__file__).parent / Path("quotes.sqlite3")
cache = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)


def get_quote(quote_id: str) -> str:
    out = []
    quote = cache.get(f"{CACHE_KEY_PREFIX}.{quote_id}")

    if quote is None:
        # Get from the database
        try:
            with sqlite3.connect(DB_PATH) as db:
                cursor = db.cursor()
                res = cursor.execute(
                    f"SELECT text FROM quotes WHERE id = {quote_id}"
                ).fetchone()
                if not res:
                    return "There was no quote stored matching that id!"

                quote = res[0]
                out.append(f"Got '{quote}' FROM DB")
        except Exception as e:
            print(e)

        # Add to the cache
        key = f"{CACHE_KEY_PREFIX}.{quote_id}"
        cache.set(key, quote, ex=60)
        out.append(f"Added TO CACHE, with key '{key}'")
    else:
        out.append(f"Got '{quote}' FROM CACHE")

    if out:
        return " - ".join(out)


def main():
    while True:
        quote_id = input("Enter the ID of the quote: ")
        if quote_id.isdigit():
            out = get_quote(quote_id)
            print(out)
        else:
            print("You must enter a number. Please retry.")


if __name__ == "__main__":
    main()
