import json
import xml.etree.ElementTree as etree
import os
import sys


def extract_json(filepath: str):
    with open(filepath, mode="r", encoding="utf-8") as f:
        return json.load(f)


def extract_xml(filepath: str):
    return etree.parse(filepath)


def extract(selected_factory):
    dirname = os.path.split(os.path.abspath(__file__))[0]

    if selected_factory == "json":
        factory = extract_json
        parsed_data = factory(os.path.join(dirname, "movies.json"))

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
    elif selected_factory == "xml":
        factory = extract_xml
        parsed_data = factory(os.path.join(dirname, "person.xml"))

        selection = parsed_data.findall(f".//person[lastName='Liar']")
        for idx, item in enumerate(selection, start=1):
            firstname = item.find("firstName").text
            lastname = item.find("lastName").text
            print(f"{idx}. {firstname} {lastname}")
            for p in item.find("phoneNumbers"):
                print(f"   phone number ({p.attrib['type']}): {p.text}")


if __name__ == "__main__":
    print("*** JSON case ***")
    extract(selected_factory="json")
    print()
    print("*** XML case ***")
    extract(selected_factory="xml")
