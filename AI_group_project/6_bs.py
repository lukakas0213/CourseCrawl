import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")  # lxml parser를 사용해서 soup 객체 생성
print(soup.title)    # title element 전체 출력
print(soup.title.get_text())        # title element의 내용만 출력
print(soup.a)       # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs) # a element의 속성 정보 출력
print(soup.a["href"])    # a element의 href 속성 값 출력

print(soup.find("a", attrs={"class":"Nbtn_upload"}))    # class="Nbtn_upload"인 a element 찾기
print(soup.find(attrs={"class":"Nbtn_upload"}))    # class="Nbtn_upload"인 어떤 element 찾기