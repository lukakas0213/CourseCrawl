import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=783053&tab=tue"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}
res = requests.get(url, headers=headers)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")  # lxml parser를 사용해서 soup 객체 생성
