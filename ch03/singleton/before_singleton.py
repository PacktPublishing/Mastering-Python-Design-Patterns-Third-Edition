import urllib.request


class URLFetcher:
    def __init__(self):
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                page_content = response.read()
                with open("content.html", "a") as f:
                    f.write(page_content + "\n")
                self.urls.append(url)


if __name__ == "__main__":
    print(URLFetcher() is URLFetcher())
