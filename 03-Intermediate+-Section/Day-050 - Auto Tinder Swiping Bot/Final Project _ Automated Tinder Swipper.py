from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

URL = "https://tinder.com/"
chrome_driver_path = "C:/chromedriver.exe"

# USERNAME = os.environ.get("USERNAME")
# PASSWORD = os.environ.get("PASSWORD")
PHONE_NUMBER = "729339635"

# open Tinder
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)
driver.maximize_window()

# login 
time.sleep(5)
login_button = driver.find_element(By.LINK_TEXT, value="Log in")
login_button.click()

time.sleep(5)
tel_login = driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button")
tel_login.click()

time.sleep(5)
tel_input = driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/input")
tel_input.send_keys(PHONE_NUMBER)
tel_input.send_keys(Keys.RETURN)

# Verification
time.sleep(5)
input("Click Enter after Verification")



input()
