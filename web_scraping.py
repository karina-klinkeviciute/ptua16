from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special text">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <a href="https://www.google.com">Hyperlink</a>
  <br/>
  <div data-example="yes">bye</div>
</body>
</html>
"""


soup = BeautifulSoup(html, "html.parser")

# print(type(soup))

print(soup.body)

print(soup.body.div)

print(type(soup.body))

print(soup.find("div"))

print(soup.find_all(class_="special"))

print(soup.find_all(attrs={"data-example": "yes"}))

items_by_ids = soup.select("#first")

print(items_by_ids)

items_by_classes = soup.select(".special")

print(items_by_classes)

items_by_div_tag = soup.select("div")

print(items_by_div_tag)

items_by_attr = soup.select("[data-example]")

print(items_by_attr)

texts = soup.select(".special")

item = texts[0]

print(item.get_text())

for item in soup.select(".special"):
    print(item.get_text())
    print(item.name)
    print(item.attrs)

first_div = soup.select("div")[0]

id_attribute = first_div["id"]

print(id_attribute)

print(type(first_div))

url = soup.find("a")["href"]

print(url)


print(soup.div.contents)

li_item = soup.find("li")

print(li_item.next_sibling.next_sibling)

print(li_item.parent.parent)

li_item_2 = li_item.find_next_sibling()

print(li_item_2)

li_items_3 = li_item.find_next_siblings()

print(li_items_3)

print(li_item.find_parent().find_previous_sibling())

soup.body.next_element.next_element.next_element.next_element.get_text()

