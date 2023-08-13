import json
from pprint import pprint

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://datki.net/komplimenti/podruge/prikolnie/"


def get_soup(url: str) -> BeautifulSoup:
    """Get soup of page by it's url."""
    html = requests.get(url).text
    return BeautifulSoup(html, "html.parser")


def replace_br(text):
    return str(text).replace("<br/>", "\n").replace("<p>", "").replace("</p>", "")


def get_compliments(url: str = BASE_URL):
    soup = get_soup(url)

    result = []

    wrapper = soup.find("div", class_="content-entry-wrap")
    articles = wrapper.find_all("div", class_="entry-summary")
    inner_items = [item.find_all("p") for item in articles]
    for items in inner_items:
        wrap = []
        for item in items:
            wrap.append(replace_br(item))
        result.append(wrap)

    return result


compliments = get_compliments() + get_compliments("https://datki.net/komplimenti")

with open("compliments.json", mode="w", encoding="utf-8") as file:
    json.dump(
        compliments,
        file,
        indent=4,
        ensure_ascii=False,
    )
