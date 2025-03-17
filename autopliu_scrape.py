from random import choice

import requests

from bs4 import BeautifulSoup

# page_number = 1
#
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
# ]
#
# headers = {"User-Agent": choice(user_agents)}
#
# source = requests.get(f"https://en.autoplius.lt/ads?vip=1&page_nr={page_number}/", headers=headers).text
#
# soup = BeautifulSoup(source, "html.parser")
#
# print(soup)


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.autoplius.lt/ads?vip=1&page_nr={page_number}/")

# Wait for content to load, interact, etc.
print(driver.page_source)
driver.quit()

soup = BeautifulSoup(driver.page_source, "html.parser")

anouncements = soup.find_all("div", {"class": "announcement-body"})

for anouncement in anouncements:
    print(anouncement.text)
