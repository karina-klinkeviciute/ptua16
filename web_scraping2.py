import csv

import requests

from bs4 import BeautifulSoup

source = requests.get("https://www.cnn.com/").text

# print(source)

soup = BeautifulSoup(source, "html.parser")

block = soup.find("h2")

if block:
    print(block.text.strip())
else:
    print("Couldn't find the specified block. The class or tag might have changed.")

block = soup.find(class_="container__title")

text = block.find("h2").text.strip()
print(f"Headline: {text}")

link_tag = block.find("a")

if link_tag:
    link = link_tag.get("href")
    if link:
        if not link.startswith("http"):
            link = "https://www.cnn.com" + link

    print(f"Link: {link}")

else:
    print("Couldn't find the specified link. The class or tag might have changed.")

blocks = soup.find_all(class_="container__headline-text")

for block in blocks:
    text = block.text.strip()
    print(f"Headline: {text}")

with open("headlines.csv", "w", encoding="UTF-8", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["WEBSITE", "HEADLINE"])

    for block in blocks:
        try:
            text = block.text.strip()
            csv_writer.writerow(["CNN", text])
        except:
            pass
