from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

# print(response.text)

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    article = article.find("a")
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

max_index = article_upvotes.index(max(article_upvotes))
print(f"{article_texts[max_index]}\t{article_upvotes[max_index]}")










# import lxml

# with open("website.html", encoding="utf8") as file:
#     content = file.read()
#
# soup = BeautifulSoup(content, "html.parser")
#
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # print(soup.prettify())
#
# # print(soup.a)
#
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     pass
#
# # print(all_anchor_tags)
#
# # heading = soup.find(name="h1", id="name")
# # print(heading)
#
# # heading = soup.find(name="h3", class_="heading")
# # print(heading.getText())
#
# company_link = soup.select_one(selector="p a")
# print(company_link)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

