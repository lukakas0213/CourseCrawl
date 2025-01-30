import pickle
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import subprocess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 설정
options = Options()
options.add_experimental_option("detach", True)

# 브라우저 실행
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# 수강신청 페이지로 이동
url = "https://app.testudo.umd.edu/#/main/dropAdd?termId=202501"
browser.get(url)

# 로그인 정보 입력
username_input = browser.find_element(By.ID, "username")
username_input.send_keys("dpark021")  # 입력할 사용자명

password_input = browser.find_element(By.NAME, "j_password")
password_input.send_keys("Pdh02130213!")  # 입력할 비밀번호

login_button = browser.find_element(By.XPATH, "//button[@type='submit' and @name='_eventId_proceed']")
login_button.click()

time.sleep(10)
def press_escape_key():
    applescript = '''
    tell application "System Events"
        key code 53  -- ESC 키
    end tell
    '''
    subprocess.run(['osascript', '-e', applescript])

# ESC 키 눌러주는 함수 실행
press_escape_key()

time.sleep(4)
press_escape_key()

body = browser.find_element(By.TAG_NAME, "body")  # body 태그 선택
body.send_keys(Keys.ESCAPE)  # ESC 키 보내기

# Duo 인증을 수동으로 완료한 후 쿠키 저장
# time.sleep(10)  # Duo 인증을 완료할 시간을 주고

# 'Other options' 링크 클릭
try:
    other_options_link = browser.find_element(By.CLASS_NAME, "action-link.other-options-link")
    other_options_link.click()
    print("Other options 링크를 클릭했습니다.")
except Exception as e:
    print(f"링크 클릭 중 오류 발생: {e}")

time.sleep(3)
try:
    # "Duo Push" 텍스트가 있는 요소 찾기
    duo_push_link = browser.find_element(By.XPATH, "//div[@class='row display-flex method-label' and text()='Duo Push']")
    duo_push_link.click()
    print("Duo Push를 클릭했습니다.")
except Exception as e:
    print(f"클릭 중 오류 발생: {e}")
# Duo 푸시 인증 대기
try:
    # Duo Push 버튼 클릭 (알림을 보냄)
    duo_push_button = WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "auth-method auth-method-link display-flex flex-wrap-nowrap align-flex-justify-content-start"))
    )
    duo_push_button.click()
    print("Duo Push 인증을 클릭했습니다.")
    
    # 핸드폰에서 Duo 인증을 완료하고, 페이지가 갱신될 때까지 대기
    WebDriverWait(browser, 60).until(
        EC.url_changes(browser.current_url)  # 현재 URL이 변경될 때까지 대기
    )
    print("Duo 인증 완료 후 페이지가 갱신되었습니다.")
    
except Exception as e:
    print(f"Duo 인증 중 오류 발생: {e}")


try:
    # "Yes, this is my device" 버튼 찾기
    trust_button = browser.find_element(By.ID, "trust-browser-button")
    trust_button.click()
    print("Yes, this is my device 버튼을 클릭했습니다.")
except Exception as e:
    print(f"버튼 클릭 중 오류 발생: {e}")

time.sleep(3)
# try:
#     # 'Student Schedule' 클릭 (CSS selector 사용)
#     student_schedule_span = browser.find_element(By.CSS_SELECTOR, "span.ng-binding")
#     student_schedule_span.click()
#     print("Student Schedule 버튼을 클릭했습니다.")
# except Exception as e:
#     print(f"버튼 클릭 중 오류 발생: {e}")

# try:
#     # 'Registration - Drop/Add' 링크 클릭
#     drop_add_link = browser.find_element(By.XPATH, "//a[@id='Registration - Drop/Add' and @class='header-dropdown-item ng-binding ng-scope']")
#     drop_add_link.click()
#     print("Registration - Drop/Add 링크를 클릭했습니다.")
# except Exception as e:
#     print(f"링크 클릭 중 오류 발생: {e}")
# href 속성에서 URL을 가져와 직접 이동
url = "https://app.testudo.umd.edu/#/main/dropAdd?termId=202501"  # 링크에서 가져온 URL
browser.get(url)
print("링크로 이동했습니다.")

time.sleep(3)
# 버튼을 ng-click을 기준으로 찾아 클릭
while True:  # Infinite loop for continuous checking
    try:
        # Click "Spring 2025" button
        spring_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@ng-click='getDropAddInfo(term)' and contains(text(), 'Spring 2025')]"))
        )
        spring_button.click()
        print("Spring 2025 버튼을 클릭했습니다.")

        time.sleep(3)

        # Check for "Sign out and reload" button
        try:
            sign_out_button = browser.find_element(By.XPATH, "//button[@ng-click='signOffAndReload()' and contains(text(), 'Sign out and reload')]")
            sign_out_button.click()
            print("Sign out and reload 버튼을 클릭했습니다.")
            time.sleep(3)
        except Exception as e:
            print("Sign out and reload 버튼이 존재하지 않거나 클릭할 수 없습니다:", e)

        TOKEN = '7767421130:AAGTdmCNuClqEi9kYOET6c_RZKOwUnIl-HM'
        CHAT_ID = '7580293509'  # 올바른 채팅 ID 입력
        TELEGRAM_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        
        # Find and input course code
        course_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@ng-model='pendingCourse.course']"))
        )
        course_input.click()
        course_input.clear()
        course_input.send_keys("CMSC351")
        print("과목 코드 'CMSC351'이 입력되었습니다.")

        time.sleep(3)

        # Click "Submit Changes" button
        try:
            submit_button = browser.find_element(By.ID, "submit_changes")
            if submit_button.is_enabled():
                submit_button.click()
                print("Submit Changes 버튼을 클릭했습니다.")
            else:
                print("Submit Changes 버튼이 비활성화되어 있습니다.")
        except Exception as e:
            print("버튼 클릭 중 오류 발생:", e)

        # Check for "Closed" status
        section_status_elements = WebDriverWait(browser, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//td[@class='drop-add-transaction-table-seatsRemain']/span"))
        )
        section_statuses = [el.text.strip() for el in section_status_elements]
        print("Extracted Statuses:", section_statuses)  # Debugging output

        # Find open sections
        open_sections = [status for status in section_statuses if status and status != "Closed"]
        if len(open_sections) >= 2:  # Alert only when two or more sections are open
            message = f"🚨 {len(open_sections)} sections are now OPEN! Available seats: {', '.join(open_sections)}. Check registration now!"
            payload = {'chat_id': CHAT_ID, 'text': message}
            response = requests.post(TELEGRAM_URL, data=payload)

            if response.status_code == 200:
                print("✅ Alert sent successfully!")
            else:
                print("❌ Failed to send alert:", response.text)
        else:
            print("Less than 2 sections open. No action taken.")

    except Exception as e:
        print("❌ Error during execution:", e)

    # Refresh the page and wait 1 minute before repeating
    browser.refresh()
    print("🔄 페이지 새로고침 후 1분 대기 중...")
    
    def press_enter_mac():
        applescript = '''
        tell application "System Events"
            key code 36  -- Presses the Enter/Return key
        end tell
        '''
        subprocess.run(['osascript', '-e', applescript])

    # Example usage
    press_enter_mac()

    time.sleep(60)  # Wait for 1 minute before next attempt

