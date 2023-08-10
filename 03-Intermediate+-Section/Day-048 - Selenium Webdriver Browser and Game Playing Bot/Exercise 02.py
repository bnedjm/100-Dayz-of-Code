from selenium import webdriver
from selenium.webdriver.chrome.service import Service

URL = "https://en.m.wikipedia.org/wiki/Main_Page"

chrome_driver_path = "C:/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)

articles_count = driver.find_element(by="xpath", value="//*[@id='articlecount']/a[1]")
print(articles_count.text)

