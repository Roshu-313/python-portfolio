import requests
from bs4 import BeautifulSoup

print("Starting web scraper...")

url = "https://news.ycombinator.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("a", class_="storylink")

for index, title in enumerate(titles, start=1):
    print(index, title.text)
