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


def extract(selected_factory):
    dirname = os.path.split(os.path.abspath(__file__))[0]

    if selected_factory == "json":
        try:
            factory = dataextraction_factory(os.path.join(dirname, "movies.json"))

            json_data = factory.parsed_data
            print(f"Found: {len(json_data)} movies")
            for movie in json_data:
                print(f"- Title: {movie['title']}")
            year = movie["year"]
            if year:
                print(f"  Year: {year}")
            director = movie["director"]
            if director:
                print(f"  Director: {director}")
            genre = movie["genre"]
            if genre:
                print(f"  Genre: {genre}")
        except ValueError as e:
            print(e)
    elif selected_factory == "xml":
        try:
            factory = dataextraction_factory(os.path.join(dirname, "person.xml"))

            xml_data = factory.parsed_data
            liars = xml_data.findall(f".//person[lastName='Liar']")
            print(f"found: {len(liars)} persons")
            for liar in liars:
                firstname = liar.find("firstName").text
                lastname = liar.find("lastName").text
                print(f"- {lastname}")
                print(f"  first name: {firstname}")
                print(f"  last name: {lastname}")
                [
                    print(f"  phone number ({p.attrib['type']}):", p.text)
                    for p in liar.find("phoneNumbers")
                ]
        except ValueError as e:
            print(e)
    elif selected_factory == "sq3":
        try:
            factory = dataextraction_factory(os.path.join(dirname, "person.sq3"))
        except ValueError as e:
            print(e)
    else:
        print("Input invalid")


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Retry! Example usage: python ch3/factory_method.py json")
        sys.exit(1)

    args = sys.argv[1:]
    extract(selected_factory=args[0])
