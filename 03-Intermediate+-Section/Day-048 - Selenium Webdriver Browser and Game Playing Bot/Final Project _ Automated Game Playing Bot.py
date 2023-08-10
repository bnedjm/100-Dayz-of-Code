from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.service import Service
import time

URL = "http://orteil.dashnet.org/experiments/cookie/"
INTERVAL = 5
ENDTIME = 5*60

def find_store_elements():
    # store elements
    store_elements = []
    # buyTime_machine = driver.find_element(by="id", value="buyTime machine")  # 123456789
    store_elements.append(
        {
            "id": "buyTime machine",
            # "object": buyTime_machine,
            "cost": 123456789,
        }
    )
    # buyPortal = driver.find_element(by="id", value="buyPortal")  # 1000000
    store_elements.append(
        {
            "id": "buyPortal",
            # "object": buyPortal,
            "cost": 100000,
        }
    )
    # buyAlchemy_lab = driver.find_element(by="id", value="buyAlchemy lab")  # 50000
    store_elements.append(
        {
            "id": "buyAlchemy lab",
            # "object": buyAlchemy_lab,
            "cost": 50000,
        }
    )
    # buyShipment = driver.find_element(by="id", value="buyShipment")  # 7000
    store_elements.append(
        {
            "id": "buyShipment",
            # "object": buyShipment,
            "cost": 7000,
        }
    )
    # buyMine = driver.find_element(by="id", value="buyMine")  # 2000
    store_elements.append(
        {
            "id": "buyMine",
            # "object": buyMine,
            "cost": 2000,
        }
    )
    # buyFactory = driver.find_element(by="id", value="buyFactory")  # 500
    store_elements.append(
        {
            "id": "buyFactory",
            # "object": buyFactory,
            "cost": 500,
        }
    )
    # buyGrandma = driver.find_element(by="id", value="buyGrandma")  # 100
    store_elements.append(
        {
            "id": "buyGrandma",
            # "object": buyGrandma,
            "cost": 100,
        }
    )
    # buyCursor = driver.find_element(by="id", value="buyCursor")  # 15
    store_elements.append(
        {
            "id": "buyCursor",
            # "object": buyCursor,
            "cost": 15,
        }
    )
    return store_elements


def upgrade_manager(store_elements_):
    # money element
    money = driver.find_element(by="id", value="money")

    for store_element in store_elements_:
        if int(money.text) >= store_element["cost"]:
            try:
                driver.find_element(by="id", value=store_element["id"]).click()
            except StaleElementReferenceException:
                continue


chrome_driver_path = "C:/chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(URL)

# element to click
cookie = driver.find_element(by="id", value="cookie")

five_sec = time.time() + INTERVAL
five_min = time.time() + ENDTIME

while True:
    cookie.click()
    if time.time() >= five_sec:
        store_elements = find_store_elements()
        upgrade_manager(store_elements)
        # update reference
        INTERVAL += 0.05
        five_sec = time.time() + INTERVAL
    if time.time() >= five_min:
        cps = driver.find_element(by="id", value="cps")
        print(f"cookies/second = {cps.text}")
        break
