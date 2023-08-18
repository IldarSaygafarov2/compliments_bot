import json


def read_json(filename: str):
    with open(filename, mode="r", encoding="utf-8") as file:
        content = json.load(file)
    return content


def read_file(filename: str):
    with open(filename, mode="r", encoding="utf-8") as file:
        content = file.read().split("=")
        result = list(filter(lambda x: x != '', content))
    return result


