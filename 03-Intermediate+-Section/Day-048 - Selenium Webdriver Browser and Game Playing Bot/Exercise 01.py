from selenium import webdriver
from selenium.webdriver.chrome.service import Service

URL = "https://www.python.org/"

chrome_driver_path = "C:/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)

upcoming_events_raw = driver.find_elements(by="xpath", value="//*[@id='content']/div/section/div[2]/div[2]/div/ul/li")
upcoming_events_dicts = [{"time":item.text.split("\n")[0], "name":item.text.split("\n")[1]} for item in upcoming_events_raw]

print(upcoming_events_dicts)
