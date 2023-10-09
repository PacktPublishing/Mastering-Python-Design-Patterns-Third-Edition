import json
import xml.etree.ElementTree as etree
import os
from typing import Callable


def extract_json(filepath: str):
    with open(filepath, mode="r", encoding="utf-8") as f:
        return json.load(f)


def extract_xml(filepath: str):
    return etree.parse(filepath)


def extract(factory: Callable):
    dirname = os.path.split(os.path.abspath(__file__))[0]

    if factory == extract_json:
        path = os.path.join(dirname, "movies.json")
        data = factory(path)

        for idx, movie in enumerate(data, start=1):
            print(f"{idx}. {movie['title']}")
        year = movie["year"]
        if year:
            print(f"   Year: {year}")
        director = movie["director"]
        if director:
            print(f"   Director: {director}")
        genre = movie["genre"]
        if genre:
            print(f"   Genre: {genre}")
    elif factory == extract_xml:
        path = os.path.join(dirname, "person.xml")
        data = factory(path)

        search_xpath = ".//person[lastName='Liar']"
        items = data.findall(search_xpath)
        for idx, item in enumerate(items, start=1):
            firstname = item.find("firstName").text
            lastname = item.find("lastName").text
            print(f"{idx}. {firstname} {lastname}")
            for p in item.find("phoneNumbers"):
                number_type = p.attrib["type"]
                number_val = p.text
                phone = f"{number_type}: {number_val}"
                print(f"   {phone}")


if __name__ == "__main__":
    print("*** JSON case ***")
    extract(factory=extract_json)
    print()
    print("*** XML case ***")
    extract(factory=extract_xml)
