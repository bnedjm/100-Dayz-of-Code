import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
empire_website = response.text

soup = BeautifulSoup(empire_website, "html.parser")

titles = [title.getText() for title in soup.find_all(name="h3", class_="title")]
titles.reverse()

with open("100 Best Movies.txt", "w", encoding="utf8") as file:
    for title in titles:
        file.write("%s\n" % title)
