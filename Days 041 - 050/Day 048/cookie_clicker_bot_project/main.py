from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")
driver.maximize_window()

cookie = driver.find_element(By.ID, "cookie")
cookie_count = driver.find_element(By.ID, "money")
items = [driver.find_element(By.ID, "store").text]

for item in items:
    print(item)



def click_cookie():
    cookie.click()

def buy_item():
    for item in items:
        if cookie_count >= item:
            item.click()





while(True):
    pass