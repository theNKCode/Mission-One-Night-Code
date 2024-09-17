from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

USERNAME = "the_NKNikhil"
PASSWORD = "NKTwitter123@."
PHONE ="9309101444"
TEXT = "This is a tweet posted using Selenium!agasgfhg"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    driver.get(f"https://twitter.com/login")

    time.sleep(5)
    user_field = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input" )
    user_field.send_keys(USERNAME)
    
    next_btn = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div")
    next_btn.click()
    time.sleep(5)
    
    # phone_btn = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
    # phone_btn.send_keys(PHONE)
    
    # next1_btn = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div") 
    # next1_btn.click()
    # time.sleep(5)
    
    pass_field = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    pass_field.send_keys(PASSWORD)
    
    log_btn = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div")
    log_btn.click()

    time.sleep(10)

    tweet_field = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div")
    tweet_field.click()
    tweet_field.send_keys(TEXT)
    
    tweet_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span")
    tweet_button.click()

    time.sleep(5)

finally:
    driver.quit()
