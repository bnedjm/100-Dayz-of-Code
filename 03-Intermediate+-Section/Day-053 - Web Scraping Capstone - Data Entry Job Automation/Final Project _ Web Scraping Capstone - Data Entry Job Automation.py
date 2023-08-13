from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
import time
import os


CHROME_DRIVER_PATH = "C:/chromedriver.exe"

GOOGLE_FORM_URL = "https://forms.gle/FCpBtVfpdh9fymuq6"
ZILLOW_SEARCH_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


class DataEntry:
    def __init__(self, CDP):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=CDP)
        self.driver.maximize_window()
        self.addresses = ["test"]
        self.prices = ["test"]
        self.links = ["test"]

    def get_rentals_data(self):
        pass

    def fill_google_form(self):
        time.sleep(2)
        self.driver.get(GOOGLE_FORM_URL)
        time.sleep(10)
        for _ in range(len(self.addresses)):
            address = self.driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
            address.send_keys(self.addresses[_]) # enter the address
            time.sleep(2)
            price = self.driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            price.send_keys(self.prices[_]) # enter the price
            time.sleep(2)
            link = self.driver.find_element(By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link.send_keys(self.links[_]) # enter the link
            time.sleep(2)
            login_form = self.driver.find_element(By.ID, value="mG61Hd")
            login_form.submit() # submit
            time.sleep(5)

    # def find_followers(self):
    #     time.sleep(2)
    #     self.driver.get(f"{INSTAGRAM_URL}{INSTAGRAM_SIMILAR_ACCOUNT}")
    #     time.sleep(10)
    #     self.driver.find_element(By.XPATH, value="//li[2]/a").click() # click followers
    #     time.sleep(2)
    #     followers = int(self.driver.find_element(By.XPATH, value="//li[2]/a/span").get_attribute("title").replace(",", "")) # get number of followers
    #     followers_popup = self.driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")
    #     for _ in range(int(followers/2)): # scroll up
    #         time.sleep(2)
    #         self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)

    # def follow(self):
    #     time.sleep(2)
    #     follow_buttons = self.driver.find_elements(By.XPATH, value="//*[@class='_aano']/div[1]/div/div/div/div/div/div[3]/div/button")
    #     for follow_button in follow_buttons:
    #         time.sleep(2)
    #         try:
    #             follow_button.click() # click follow
    #         except ElementClickInterceptedException: # in case, account is already followed
    #             self.driver.find_element(By.XPATH, value="//button[text()='Cancel']").click() # click cancel unfollow
    #             time.sleep(2)
    #             follow_button.click()


bot = DataEntry(CHROME_DRIVER_PATH)
bot.get_rentals_data()
bot.fill_google_form()
bot.driver.quit()
