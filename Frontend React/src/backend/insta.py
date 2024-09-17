from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def init():
    USERNAME =  "the_nikhilkamble"
    PASSWORD =  "NKInsta235@."

    driver = webdriver.Chrome()

    driver.get('https://www.instagram.com/accounts/login/')

    time.sleep(3)

    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(USERNAME)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(5)

    driver.get('https://www.instagram.com/direct/inbox/')

    time.sleep(5)


    def send_message(username, message):
        driver.get(f'https://www.instagram.com/direct/t/{username}/')

        time.sleep(5)

        noti_turnoff = driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        noti_turnoff.click()

        time.sleep(5)
        try:
            message_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p"))
            )
            message_input.send_keys(message)
            
            message_input.send_keys(Keys.RETURN)
            send_button = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[3]" )
            
            time.sleep(2)
            
        except Exception as e:
            print(f"An error occurred: {e}")

    recipient_username = 100972247971681
    message_text = 'Hello, this is a test message!'
    send_message(recipient_username, message_text)

    driver.quit()
