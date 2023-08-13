from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time
import os


CHROME_DRIVER_PATH = "C:/chromedriver.exe"

INSTAGRAM_SIMILAR_ACCOUNT = "bal.sunder"
INSTAGRAM_URL = "https://www.instagram.com/"
INSTAGRAM_LOGIN_URL = f"{INSTAGRAM_URL}accounts/login/"
INSTAGRAM_USERNAME = os.environ.get("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.environ.get("INSTAGRAM_PASSWORD")


class InstaFollower:
    def __init__(self, CDP):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=CDP)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def login(self):
        time.sleep(2)
        self.driver.get(INSTAGRAM_LOGIN_URL)
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//button[text()='Allow all cookies']").click()
        time.sleep(2)
        username = self.driver.find_element(By.XPATH, value="//*[@id='loginForm']/div/div[1]/div/label/input")
        username.send_keys(INSTAGRAM_USERNAME) # enter the username
        password = self.driver.find_element(By.XPATH, value="//*[@id='loginForm']/div/div[2]/div/label/input")
        password.send_keys(INSTAGRAM_PASSWORD) # enter the password
        time.sleep(2)
        login_form = self.driver.find_element(By.ID, value="loginForm")
        login_form.submit() # login
        time.sleep(5)

    def find_followers(self):
        time.sleep(2)
        self.driver.get(f"{INSTAGRAM_URL}{INSTAGRAM_SIMILAR_ACCOUNT}")
        time.sleep(10)
        self.driver.find_element(By.XPATH, value="//li[2]/a").click() # click followers
        time.sleep(2)
        followers = int(self.driver.find_element(By.XPATH, value="//li[2]/a/span").get_attribute("title").replace(",", "")) # get number of followers
        followers_popup = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
        for _ in range(int(followers/2)): # scroll up
            time.sleep(2)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)

    def follow(self):
        time.sleep(2)
        follow_buttons = self.driver.find_elements(By.XPATH, value="//*[@class='_aano']/div[1]/div/div/div/div/div/div[3]/div/button")
        for follow_button in follow_buttons:
            time.sleep(2)
            try:
                follow_button.click() # click follow
            except ElementClickInterceptedException: # in case, account is already followed
                self.driver.find_element(By.XPATH, value="//button[text()='Cancel']").click() # click cancel unfollow
                time.sleep(2)
                follow_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
bot.driver.quit()
