import json


def read_json(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        content = json.load(file)
    return content
