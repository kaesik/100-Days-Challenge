from bs4 import BeautifulSoup
import requests as rq

response = rq.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
title = soup.find(name="span", class_="titleline")
title_text = title.getText()
title_link = title.find(name="a").get("href")
title_upvotes = soup.find(name="span", class_="score").getText()
print(title_text, title_link, title_upvotes)

articles = soup.find_all(name="span", class_="titleline")
ar_texts = []
ar_links = []

for tag in articles:
    text = tag.getText()
    ar_texts.append(text)

    link = tag.find(name="a").get("href")
    ar_links.append(link)

ar_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(ar_texts)
print(ar_links)
print(ar_upvotes)

largest_num = max(ar_upvotes)
largest_num_i = ar_upvotes.index(largest_num)

print(ar_texts[largest_num_i])
print(ar_links[largest_num_i])