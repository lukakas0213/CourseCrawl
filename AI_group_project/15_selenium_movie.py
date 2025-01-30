from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

# Set up Chrome options and add the detach option
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Set up Chrome with Service and DriverManager
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

browser.maximize_window() #창 최대화

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"
            ,"Accept-Language" : "ko-KR,ko"
            }

url = "https://play.google.com/store/movies?hl=kr_KO"
browser.get(url) #url로 이동

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "ULeU3b neq64b"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class" : "Epkrse "}).text
    print(title)