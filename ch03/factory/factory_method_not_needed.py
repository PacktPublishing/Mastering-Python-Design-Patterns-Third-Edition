import json
import xml.etree.ElementTree as ET

from pathlib import Path


class JSONDataExtractor:
    def __init__(self, filepath: Path):
        self.data = {}
        with open(filepath) as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath: Path):
        self.tree = ET.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def extract(case: str):
    pathname = Path(__file__)
    dir_path = pathname.parent

    if case == "json":
        path = dir_path / Path("movies.json")
        data = JSONDataExtractor(path).parsed_data

        for movie in data:
            print(f"- {movie['title']}")
            director = movie["director"]
            if director:
                print(f"   Director: {director}")
            genre = movie["genre"]
            if genre:
                print(f"   Genre: {genre}")
    elif case == "xml":
        path = dir_path / Path("person.xml")
        data = XMLDataExtractor(path).parsed_data

        search_xpath = ".//person[lastName='Liar']"
        items = data.findall(search_xpath)
        for item in items:
            first = item.find("firstName").text
            last = item.find("lastName").text
            print(f"- {first} {last}")
            for pn in item.find("phoneNumbers"):
                pn_type = pn.attrib["type"]
                pn_val = pn.text
                phone = f"{pn_type}: {pn_val}"
                print(f"   {phone}")


if __name__ == "__main__":
    print("* JSON case *")
    extract(case="json")
    print("* XML case *")
    extract(case="xml")
