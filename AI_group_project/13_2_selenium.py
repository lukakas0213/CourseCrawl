from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Set up Chrome options and add the detach option
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Set up Chrome with Service and DriverManager
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# 네이버로 이동
browser.get("http://www.naver.com")

# 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
elem.click()

# 로그인 정보 입력
browser.find_element(By.CLASS_NAME, "input_id").send_keys("furjfurjfurj")
browser.find_element(By.CLASS_NAME, "input_pw").send_keys("Pdh02130213!")

# 로그인 버튼 클릭
browser.find_element(By.CLASS_NAME, "btn_login").click()

browser.close()