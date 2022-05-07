import requests
from bs4 import BeautifulSoup as bs

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
response = requests.get(url)
html = response.text
soup = bs(html, "html.parser")

