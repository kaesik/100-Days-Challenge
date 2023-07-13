import os
import requests as rq
import spotipy as sp
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# date = input("Which year do you want to travel to? (YYY-MM-DD): ")
date = "2000-10-01"
year = date.split("-")[0]
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URL = "https://example.com/callback"

spotify = sp.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URL,
    scope="playlist-modify-private playlist-read-private",
    show_dialog=True,
    cache_path="token.txt",))
user_id = spotify.current_user()["id"]


response = rq.get(URL)
hot_100 = response.text
soup = BeautifulSoup(hot_100, "html.parser")
titles = soup.find_all(name="h3", class_="a-no-trucate", id="title-of-a-story")
artists = soup.find_all(name="span", class_="a-no-trucate")

titles_list = [title.getText().replace("\n", "").replace("\t", "") for title in titles]
artists_list = [artist.getText().replace("\n", "").replace("\t", "") for artist in artists]
song_list = dict(zip(artists_list, titles_list))

# for index, title in enumerate(titles_list):
#     print(f"{index+1}) {title} - {artists_list[index]}")

uri_list = []
for i, title in enumerate(titles_list):
    spotify_result = spotify.search(q=f"track:{title}", type="track")
    try:
        uri = spotify_result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")


my_playlist = spotify.user_playlist_create(user=f"{user_id}",
                                           name=f"Top 100 '{year}' Billboard Tracks",
                                           public=False,
                                           description=f"Top 100 Billboard Tracks from {year}y, created by Python.")
spotify.playlist_add_items(playlist_id=my_playlist["id"], items=uri_list)