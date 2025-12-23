import requests
from bs4 import BeautifulSoup

print("Starting web scraper...")

url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.select(".titleline a")

with open("headlines.txt", "w", encoding="utf-8") as file:
    for index, title in enumerate(titles, start=1):
        file.write(f"{index}. {title.text}\n")

print("Headlines saved to headlines.txt")
