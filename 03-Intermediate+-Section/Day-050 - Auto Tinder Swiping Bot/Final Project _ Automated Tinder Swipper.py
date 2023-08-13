from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

URL = "https://tinder.com/"
CHROME_DRIVER_PATH = "C:/chromedriver.exe"
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

# open Tinder
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options=options, executable_path=CHROME_DRIVER_PATH)
driver.get(URL)
driver.maximize_window()

# login using phone number
time.sleep(5)
login_button = driver.find_element(By.LINK_TEXT, value="Log in") # click log in button
login_button.click()
time.sleep(5)
tel_login = driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button") # click log in with phone number
tel_login.click()
input("Click Enter after Verification") # verification
time.sleep(5)
tel_input = driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div[1]/div[1]/div/div[2]/div/div[2]/div/div[2]/input")
tel_input.send_keys(PHONE_NUMBER) # enter phone number
time.sleep(2)
tel_input.send_keys(Keys.RETURN)
input("Click Enter after Verification") # verification

# dismiss all pop-ups
time.sleep(5)
driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div/div/div/div[3]/button[1]").click() # click allow for location
time.sleep(2)
driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div[2]/div/div/div[1]/div[1]/button").click() # click accept for cookies
time.sleep(2)
driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div[1]/div/div/div[3]/button[2]").click() # click not interested for notifications

# hit like
time.sleep(5)
# count = 0
for _ in range(100):
    time.sleep(2)
    driver.find_element(By.ID, value="Tinder").send_keys(Keys.ARROW_LEFT) # click left arrow - swipe left
    # try:
    #     like_button = driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div[1]/div/div/div[3]/button[2]").click() # click not interested for notifications
    # except NoSuchElementException:
    #     time.sleep(2)
    #     continue
    # except ElementClickInterceptedException:
    #     time.sleep(2)
    #     # driver.find_element(By.XPATH, value="//*[@id='u-258887019']/main/div[1]/div/div/div[3]/button[2]").click() # click back to tinder button
    # else:
    #     like_button.click() # click like button
    #     count+=1 # increase likes' count

driver.quit()
