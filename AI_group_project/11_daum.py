import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&m=&q=%EC%97%AD%EB%8C%80%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84&nzq=%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84&DA=NSJ")

soup = BeautifulSoup(res.text, "lxml") 

images = soup.find_all("img", attrs={"class":"thumb_bf"})

for image in images:
    print(image["src"])