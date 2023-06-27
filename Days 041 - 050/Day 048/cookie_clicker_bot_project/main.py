from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie = driver.find_element(By.ID, "cookie")
items = [driver.find_element(By.ID, "store").text]
upgrade = []

for item in items:
    item = item.split("\n")
    for element in item[::2]:
        element = element.split(" - ")
        upgrade.append(element)
upgrade.reverse()


def click_cookie():
    cookie.click()


def check_money(cookie_count):
    for item in upgrade:
        item[1] = item[1].replace(",", "")
        if cookie_count >= float(item[1]):
            return f"buy{item[0]}"
    return False


def buy_item(name):
    item = driver.find_element(By.ID, name)
    item.click()


def cps():
    return driver.find_element(By.ID, "cps").text


start_time = time.time()
timeout = start_time + 5
while True:
    now = time.time()
    click_cookie()
    cookie_count = float(driver.find_element(By.ID, "money").text)
    item_name = check_money(cookie_count)

    if item_name and now > timeout:
        try:
            buy_item(item_name)
        except:
            pass
        timeout = now + 5

    if now - start_time > 60*5:
        print(f"{cps()}")
        break
