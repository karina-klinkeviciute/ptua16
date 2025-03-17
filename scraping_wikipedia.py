import requests

from bs4 import BeautifulSoup

source = requests.get("https://en.wikipedia.org/wiki/Main_Page").text

# print(source)

soup = BeautifulSoup(source, "html.parser")

# print(soup)


def get_links(section, title):

    print(title)
    items = soup.find("div", {"id": section})

    list_items = items.find_all("li")

    for item in list_items:
        bold = item.find("b")
        if bold:
            link = bold.find("a")
            if link:
                href = link["href"]
                print(f"https://en.wikipedia.org{href}")

did_you_know = get_links("mp-dyk", "Did you know")


in_the_news = get_links("mp-itn", "In The News")

on_this_day = get_links("mp-otd", "On This Day")


