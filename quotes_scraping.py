import random

import requests

from bs4 import BeautifulSoup

page_number = 1

while True:

    source = requests.get(f"https://quotes.toscrape.com/page/{page_number}/").text

    # print(source)

    soup = BeautifulSoup(source, "html.parser")

    quote_blocks = soup.find_all("div", class_="quote")

    quote_block = random.choice(quote_blocks)

    quote_text = quote_block.find("span", class_="text").text

    quote_author = quote_block.find("small", class_="author").text

    print(f"This is a quote by a famous author: {quote_text}")

    guess = input("Guess who's this quote is: ")

    if guess == quote_author:
        print(f"You guessed the quote correctly!")
    else:
        print(f"You guessed the quote incorrectly!")
        names = quote_author.split()
        initials = []
        for name in names:
            initials.append(name[0])
        print("Author's initials:")
        for initial in initials:
            print(initial, " ", end="")
        print()
        guess = input("try again: ")
        if guess == quote_author:
            print(f"You guessed the quote correctly!")
        else:
            print(f"You guessed the quote incorrectly!")
            author_info_link = f"https://quotes.toscrape.com{quote_block.find('a')['href']}"
            # print(author_info_link)
            author_source = requests.get(author_info_link).text
            author_soup = BeautifulSoup(author_source, "html.parser")
            birth_date = author_soup.find("span", class_="author-born-date").text
            birth_place = author_soup.find("span", class_="author-born-location").text
            print(f"The author was born on {birth_date} in {birth_place}")
            guess = input("try again: ")
            if guess == quote_author:
                print(f"You guessed the quote correctly!")
            else:
                print(f"You guessed the quote incorrectly!")
                print(f"The author of the quote is: {quote_author}")

    cont = input("do you want to continue? (y/n)")
    if cont != "y":
        break
    else:
        page_number += 1
