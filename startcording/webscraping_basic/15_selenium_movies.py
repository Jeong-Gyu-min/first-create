import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top?hl=en_US&gl=US"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

moives = soup.find_all("div", attrs={"class":"wXUyZd"})
print(len(moives))