import os
import urllib.request
from typing import Protocol


class ResourceContentFetcher(Protocol):
    """
    Define the interface (Implementor) for implementation
    classes that help fetch content.
    """

    def fetch(self, path: str) -> str:
        ...


class ResourceContent:
    """
    Define the abstraction's interface.
    Maintain a reference to an object which represents the Implementor.
    """

    def __init__(
        self, imp: ResourceContentFetcher
    ):
        self._imp = imp

    def get_content(self, path):
        return self._imp.fetch(path)


class URLFetcher:
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def fetch(self, path):
        res = ""
        req = urllib.request.Request(path)
        with urllib.request.urlopen(
            req
        ) as response:
            if response.code == 200:
                res = response.read()
        return res


class LocalFileFetcher:
    """
    Implement the Implementor interface and define its concrete
    implementation.
    """

    def fetch(self, path):
        with open(path) as f:
            res = f.read()
        return res


def main():
    url_fetcher = URLFetcher()
    rc = ResourceContent(url_fetcher)
    res = rc.get_content("http://python.org")
    print(
        f"Fetched content with {len(res)} characters"
    )

    localfs_fetcher = LocalFileFetcher()
    rc = ResourceContent(localfs_fetcher)
    pathname = os.path.abspath(__file__)
    dir_path = os.path.split(pathname)[0]
    path = os.path.join(dir_path, "file.txt")
    res = rc.get_content(path)
    print(
        f"Fetched content with {len(res)} characters"
    )


if __name__ == "__main__":
    main()
