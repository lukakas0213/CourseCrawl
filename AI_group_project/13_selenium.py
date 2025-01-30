from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# Set up Chrome options and add the detach option
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Set up Chrome with Service and DriverManager
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Navigate to Google
browser.get("http://www.naver.com")

# elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")

# browser.back() 이전 페이지로 이동
# browser.forward() 다음 페이지로 이동
# browser.refresh() 새로고침

elem = browser.find_element(By.CLASS_NAME, "search_input")

from selenium.webdriver.common.keys import Keys
elem.send_keys("python")
elem = browser.find_element(By.XPATH, "//*[@id='search-btn']")
elem.click()
# elem.send_keys(Keys.RETURN)

for e in elem:
    e.get_attribute("href")