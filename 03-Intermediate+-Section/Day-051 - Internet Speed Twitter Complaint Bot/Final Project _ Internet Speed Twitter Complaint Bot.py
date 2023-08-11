from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import os


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/chromedriver.exe"

SPEEDTEST_URL = "http://speedtest.net/"
TWITTER_URL = "https://twitter.com/"
TWITTER_EMAIL = "boukhedenna.nedjm@gmail.com"
TWITTER_PASSWORD = "os.environ()PSWD99"



class InternetSpeedTwitterBot:
    def __init__(self, CDP):
        # service = Service(CDP)
        # self.driver = webdriver.Chrome(service=service)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=CDP)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        time.sleep(2)
        self.driver.get(SPEEDTEST_URL)
        time.sleep(2)
        self.driver.find_element(By.ID, value="onetrust-accept-btn-handler").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, value=".js-start-test").click()
        time.sleep(60)
        self.driver.find_element(By.ID, value="modal-overlay").click() #close proposition
        time.sleep(2)
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".result-data-large.number.result-data-value.upload-speed").text
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".result-data-large.number.result-data-value.download-speed").text
        print(f"{self.up} | {self.down}")


    def tweet_at_provider(self):
        time.sleep(5)
        self.driver.get(TWITTER_URL)
        time.sleep(2)
        # google_sign_in = self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[1]")
        # google_sign_in.click()
        # google_sign_in = self.driver.find_element(By.XPATH, value="//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]")
        # google_sign_in.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
# bot.tweet_at_provider()