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

url = "https://flight.naver.com/"
browser.get(url) #url로 이동

browser.find_element(By.XPATH, "//*[@id=\"__next\"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]").click()
# browser.find_element(By.XPATH, "/html/body/div/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/button/b").click()

elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/button/b")))
print(elem.text)