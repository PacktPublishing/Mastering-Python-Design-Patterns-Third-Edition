import urllib.request
from typing import Any, Dict


class SingletonType(type):
    _instances: Dict[object, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            obj = super(SingletonType, cls).__call__(*args, **kwargs)
            cls._instances[cls] = obj
        return cls._instances[cls]


class URLFetcher(metaclass=SingletonType):
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                page_content = response.read()
                with open("content.html", "a") as f:
                    f.write(str(page_content))
                self.urls.append(url)


def main():
    my_urls = [
        "http://python.org",
        "https://planetpython.org/",
        "https://www.djangoproject.com/",
    ]

    print(URLFetcher() is URLFetcher())

    fetcher = URLFetcher()
    for url in my_urls:
        fetcher.fetch(url)

    print(f"Done URLs: {fetcher.urls}")


if __name__ == "__main__":
    main()
