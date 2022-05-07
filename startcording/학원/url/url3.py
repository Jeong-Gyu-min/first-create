import requests
from bs4 import BeautifulSoup as bs

code = input("영화 코드를 입력해 주세요 >>")
url = "https://movie.naver.com/movie/bi/mi/basic.nhn"
param = {"code":code}
response = requests.get(url, params=param)
soup = bs(response.text, "html.parser")
print("제목 : " + soup.find("h3",{"class":"h_movie"}).find("a").text)
print("감독 : " + soup.find("dl",{"class":"info_spec"}).find_all("dd")[1].text)
