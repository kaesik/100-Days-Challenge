from bs4 import BeautifulSoup
import requests as rq

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = rq.get(URL)
best_movies = response.text
soup = BeautifulSoup(best_movies, "html.parser")

film_list = soup.find(name="div", class_="jsx-3523802742")
titles_list = reversed(film_list.find_all(name="img", class_="loading"))

with open("./films.txt", "w") as films:
    for index, title in enumerate(titles_list):
        title = title.get("alt")
        films.write(f"{index+1}) {title}\n")
