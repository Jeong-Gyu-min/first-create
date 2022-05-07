import requests
url ="https://www.naver.com"
param = {"query":"파이썬"}
response = requests.get(url, params=param)
print(response.text)
