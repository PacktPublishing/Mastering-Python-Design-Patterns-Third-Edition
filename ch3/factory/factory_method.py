import json
import xml.etree.ElementTree as etree
import os


class JSONDataExtractor:
    def __init__(self, filepath: str):
        self.data = {}
        with open(filepath) as f:
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
        raise ValueError(f"Cannot extract data")
    return extractor(filepath)


def extract(case: str):
    dirname = os.path.split(os.path.abspath(__file__))[0]

    if case == "json":
        try:
            path = os.path.join(dirname, "movies.json")
            factory = dataextraction_factory(path)
            data = factory.parsed_data

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
        except ValueError as e:
            print(e)
    elif case == "xml":
        try:
            path = os.path.join(dirname, "person.xml")
            factory = dataextraction_factory(path)
            data = factory.parsed_data

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
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    print("*** JSON case ***")
    extract(case="json")
    print()
    print("*** XML case ***")
    extract(case="xml")
