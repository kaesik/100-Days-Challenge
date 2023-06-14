from bs4 import BeautifulSoup
import lxml

with open("notes.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.find_all(name="a"))

for tag in soup.find_all(name="a"):
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section = soup.find(name="h3", class_="heading")
print(section.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select(".heading")
print(headings)