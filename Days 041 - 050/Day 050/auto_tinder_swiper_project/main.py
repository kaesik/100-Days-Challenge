from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

SITE = os.environ.get("SITE")
FB_EMAIL = os.environ.get("FB_EMAIL")
FB_PASSWORD = os.environ.get("FB_PASSWORD")

driver = webdriver.Chrome()
driver.get(SITE)
driver.maximize_window()


class Bot:
    def __init__(self):
        self.base_window = driver.window_handles[0]

    def accept_cookies(self):
        accept = driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
        accept.click()

    def facebook_login(self, window):
        driver.switch_to.window(window)
        cookies = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]')
        cookies.click()
        time.sleep(3)

        username = driver.find_element(By.XPATH, '//*[@id="email"]')
        username.send_keys(FB_EMAIL)
        password = driver.find_element(By.XPATH, '//*[@id="pass"]')
        password.send_keys(FB_PASSWORD)
        time.sleep(2)

        login = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        login.click()

    def accept_location(self):
        location = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
        location.click()

    def not_accept_notifications(self):
        notifications = driver.find_element(By.XPATH, '/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
        notifications.click()

    def login(self):
        login = driver.find_element(By.XPATH, '//*[@id="u490315748"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login.click()
        time.sleep(3)

        login = driver.find_element(By.XPATH, '//*[@id="u-1238065328"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
        login.click()
        time.sleep(3)

        facebook_window = driver.window_handles[1]
        self.facebook_login(facebook_window)
        time.sleep(3)

        driver.switch_to.window(self.base_window)
        time.sleep(3)

        # self.accept_location()
        # time.sleep(3)
        #
        # self.not_accept_notifications()
        # time.sleep(3)

    def like(self):
        like = ActionChains(driver)
        like.send_keys(Keys.ARROW_RIGHT)
        like.perform()

    def match(self):
        match = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[2]/main/div/div[1]/div/div[4]/button/svg/path')
        match.click()


Bot = Bot()
time.sleep(2)

Bot.accept_cookies()
Bot.login()
time.sleep(2)


while True:
    # try:
    #     Bot.like()
    #     time.sleep(1)
    # except Exception as e:
    #     print(e)
    #     time.sleep(3)
    #     continue
    pass