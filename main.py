import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def wait_for_element(driver, by, value, timeout=30):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element
    except TimeoutException:
        print(f"等待元素 {value} 超時")
        return None


def download_image(url, file_name):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            if 'image/jpeg' in content_type:
                ext = '.jpg'
            elif 'image/png' in content_type:
                ext = '.png'
            else:
                ext = '.img'
            full_file_name = f"{file_name}{ext}"
            with open(full_file_name, 'wb') as file:
                file.write(response.content)
            print(f"圖片成功下載: {full_file_name}")
        else:
            print(f"下載圖片失敗。狀態碼: {response.status_code}")
    except Exception as e:
        print(f"下載圖片時發生錯誤：{str(e)}")


def auto_login_search_and_download(url, email, account, password, article_number):
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        # chrome_options.add_argument("--headless")
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        
        email_input = wait_for_element(driver, By.ID, "username")
        if email_input:
            email_input.clear()
            email_input.send_keys(email)
        else:
            raise Exception("無法找到電子郵件輸入欄位")
        
        continue_button = wait_for_element(driver, By.XPATH, "//button[contains(text(), 'Continue')]")
        if continue_button:
            continue_button.click()
        else:
            raise Exception("無法找到繼續按鈕")
        
        input_account = wait_for_element(driver, By.ID, "userNameInput")
        if input_account:
            input_account.send_keys(account)
        else:
            raise Exception("無法找到帳號輸入欄位")
        
        input_password = wait_for_element(driver, By.ID, "passwordInput")
        if input_password:
            input_password.send_keys(password)
        else:
            raise Exception("無法找到密碼輸入欄位")
        
        sign_in_btn = wait_for_element(driver, By.ID, "submitButton")
        if sign_in_btn:
            sign_in_btn.click()
        else:
            raise Exception("無法找到登入按鈕")
        
        selector = wait_for_element(driver, By.ID, "unit-selector", timeout=60)
        if selector:
            select = Select(selector)
            select.select_by_value("zh-TW-TW")
        else:
            raise Exception("無法找到語言選擇器")
        
        time.sleep(5)
        
        for _ in range(3):
            search_input = wait_for_element(driver, By.ID, "search", timeout=20)
            if search_input:
                search_input.clear()
                search_input.send_keys(article_number)
                search_input.send_keys(Keys.ENTER)
                break
            else:
                time.sleep(2)
        else:
            raise Exception("無法找到搜尋欄位")
        
        time.sleep(5)
        
        img_element = wait_for_element(driver, By.XPATH, "//img[contains(@alt, 'FLINTAN')]")
        if img_element:
            img_src = img_element.get_attribute('src')
            download_image(img_src, f"FLINTAN_{article_number}")
        else:
            print("無法找到商品圖片")
        
        print("登入、搜尋和圖片下載過程已成功完成")
    
    except Exception as e:
        print(f"發生錯誤：{str(e)}")
        import traceback
        print("完整的錯誤追蹤：")
        print(traceback.format_exc())
    
    finally:
        if driver:
            print("按Enter鍵關閉瀏覽器...")
            input()
            driver.quit()


# 使用方法
url = "https://piafacts.ikea.net/search"
email_address = "dwhao@ikea.com.tw"
account = "IKEA\\dahao"
password = "IKtw241008"
article_number = "30489032"

auto_login_search_and_download(url, email_address, account, password, article_number)