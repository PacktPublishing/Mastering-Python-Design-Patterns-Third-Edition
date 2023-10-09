import json
import xml.etree.ElementTree as etree
import os
import sys


class JSONDataExtractor:
    def __init__(self, filepath: str):
        self.data = {}
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath: str):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def dataextraction_factory(filepath: str):
    ext = filepath.split(".")[-1]
    if ext == "json":
        extractor = JSONDataExtractor
    elif ext == "xml":
        extractor = XMLDataExtractor
    else:
        raise ValueError(f"Cannot extract data from .{ext} file")
    return extractor(filepath)


def extract(case: str):
    dirname = os.path.split(os.path.abspath(__file__))[0]

    if case == "json":
        try:
            factory = dataextraction_factory(os.path.join(dirname, "movies.json"))
            parsed_data = factory.parsed_data

            for idx, movie in enumerate(parsed_data, start=1):
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
        except ValueError as e:
            print(e)
    elif case == "xml":
        try:
            factory = dataextraction_factory(os.path.join(dirname, "person.xml"))
            parsed_data = factory.parsed_data

            selection = parsed_data.findall(f".//person[lastName='Liar']")
            for idx, item in enumerate(selection, start=1):
                firstname = item.find("firstName").text
                lastname = item.find("lastName").text
                print(f"{idx}. {firstname} {lastname}")
                for p in item.find("phoneNumbers"):
                    print(f"   phone number ({p.attrib['type']}): {p.text}")
        except ValueError as e:
            print(e)
    elif case == "sq3":
        try:
            factory = dataextraction_factory(os.path.join(dirname, "person.sq3"))
        except ValueError as e:
            print(e)
    else:
        print("Not handled; try 'json'!")


if __name__ == "__main__":
    print("*** JSON case ***")
    extract(case="json")
    print()
    print("*** XML case ***")
    extract(case="xml")
    print()
    print("*** SQ3 case ***")
    extract(case="sq3")
