from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:/chromedriver.exe"

SPEEDTEST_URL = "http://speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")


class InternetSpeedTwitterBot:
    def __init__(self, CDP):
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
        self.driver.find_element(By.ID, value="onetrust-accept-btn-handler").click() # click accept button
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, value=".js-start-test").click() # click start test button
        time.sleep(60)
        self.driver.find_element(By.ID, value="modal-overlay").click() # click overlay to dismiss promo
        time.sleep(2)
        self.up = self.driver.find_element(By.CSS_SELECTOR, value=".result-data-large.number.result-data-value.upload-speed").text # get upload speed
        self.down = self.driver.find_element(By.CSS_SELECTOR, value=".result-data-large.number.result-data-value.download-speed").text # get download speed

    def tweet_at_provider(self):
        time.sleep(2)
        self.driver.get(TWITTER_URL)
        # log in to twitter
        time.sleep(5)
        email = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email.send_keys(TWITTER_EMAIL) # enter email 
        time.sleep(2)
        email.send_keys(Keys.RETURN)
        try:
            time.sleep(5)
            username = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
        except NoSuchElementException:
            pass
        else:
            username.send_keys(TWITTER_USERNAME) # enter username 
            time.sleep(2)
            username.send_keys(Keys.RETURN)
        time.sleep(5)
        password = self.driver.find_element(By.XPATH, value="//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD) # enter password 
        time.sleep(2)
        password.send_keys(Keys.RETURN)
        # post a tweet
        time.sleep(5)
        twitter_post = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        self.driver.find_element(By.CSS_SELECTOR, value=".public-DraftStyleDefault-block.public-DraftStyleDefault-ltr").send_keys(twitter_post) # write the post
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, value=".css-18t94o4.css-1dbjc4n.r-l5o3uw.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19u6a5r" \
                                 ".r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr").click() # click post button
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
if PROMISED_UP > float(bot.up) or PROMISED_DOWN > float(bot.down):
    bot.tweet_at_provider()
else:
    bot.driver.quit()
