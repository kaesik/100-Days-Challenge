from bs4 import BeautifulSoup
import requests as rq
import spotipy as sp
import os

# date = input("Which year do you want to travel to? (YYY-MM-DD): ")
date = "2000-10-01"
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

response = rq.get(URL)
hot_100 = response.text
soup = BeautifulSoup(hot_100, "html.parser")
titles = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
artists = soup.find_all(name="span", class_="a-no-trucate")

titles_list = [title.getText().replace("\n", "").replace("\t", "") for title in titles]
artists_list = [artist.getText().replace("\n", "").replace("\t", "") for artist in artists]

for index, title in enumerate(titles_list):
    print(f"{index+1}) {title} - {artists_list[index]}")