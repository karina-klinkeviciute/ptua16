import csv

import requests

from bs4 import BeautifulSoup

source = requests.get("https://www.varle.lt/").text

# print(source)

soup = BeautifulSoup(source, "html.parser")

blocks = soup.find_all(class_="product-info")

for block in blocks:
    # print(block.text.strip())
    # print(block.contents)

    print(block.a.text)

    price_block = block.find_next_sibling().find_next_sibling()
    print(price_block.text)
    # price = price_block.find(class_="price-value")

    # print(price.text)

    # title = block.text.strip()

    # print(title)
    # price_span = block.find(class_="price_container").div.div.span.span.text.strip()
    # print(price_span)

