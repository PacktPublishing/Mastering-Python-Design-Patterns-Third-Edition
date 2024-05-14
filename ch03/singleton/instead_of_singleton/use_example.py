import example


for url in [
    "http://python.org",
    "https://planetpython.org/",
    "https://www.djangoproject.com/",
]:
    example.fetcher.fetch(url)

print(f"Done URLs: {example.fetcher.urls}")
