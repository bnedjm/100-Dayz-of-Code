from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3687871543&f_LF=f_AL&geoId=105072130&keywords=python" \
      "%20developer&location=Poland&refresh=true "
chrome_driver_path = "C:/chromedriver.exe"

USERNAME = "boukhedenna.nedjm@gmail.com"
PASSWORD = "Nedjm@2021!"


def save_job_and_follow_company():
    pass


# open LinkedIn
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)
driver.maximize_window()

# click sign in button
time.sleep(2)
sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[3]/header/nav/div/a[2]")
sign_in_button.click()

# sign in
time.sleep(2)
username = driver.find_element(By.ID, value="username")
username.send_keys(USERNAME)
password = driver.find_element(by="id", value="password")
password.send_keys(PASSWORD)
password.send_keys(Keys.RETURN)

# CAPTCHA
time.sleep(2)
input("Click enter after CAPTCHA")

# ---------------------------------------------------------#
# save all jobs and follow the company that posted each of them
jobs_list = driver.find_element(by="xpath", value="//*[@id='main']/div/div[1]/div/ul")
jobs = jobs_list.find_elements(by="tag name", value="a")

for job in jobs:
    # print(job.get_attribute("outerHTML"))
    job.click()
    time.sleep(1)
    try:
        save_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-save-button")
        print(save_button.get_attribute("outerHTML"))
    except NoSuchElementException:
        try:
            save_button = driver.find_element(By.XPATH, value="//*[@class='mt5']/div/button")
        except NoSuchElementException:
            continue
        else:
            save_button.click()
            time.sleep(5)
    else:
        save_button.click()
        time.sleep(5)
# ---------------------------------------------------------#

# close browser after 5 sec from ENTER key press
input()
time.sleep(5)
driver.quit()
