import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top?hl=en_US&gl=US"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
moives = soup.find_all("div", "class":"wXUyZd")

print(len(moives))
