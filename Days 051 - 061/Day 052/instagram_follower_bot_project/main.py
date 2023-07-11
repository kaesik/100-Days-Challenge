from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

SITE = os.environ.get("INSTAGRAM_SITE")
IG_EMAIL = os.environ.get("IG_EMAIL")
IG_PASSWORD = os.environ.get("IG_PASSWORD")
ACCOUNT = "python.hub"




class InstagramFollowerBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_window = self.driver.window_handles[0]

    def login(self):
        self.driver.get(SITE)
        self.driver.maximize_window()
        time.sleep(2)

        accept = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        accept.click()
        time.sleep(2)

        email = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        email.send_keys(IG_EMAIL)
        password = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password.send_keys(IG_PASSWORD)
        login = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button')
        login.click()
        time.sleep(6)

        not_now = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        not_now.click()
        time.sleep(3)

        notifications = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        notifications.click()
        time.sleep(3)

    def find_followers(self):
        find = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[2]/div/div/span/span')
        find.click()
        time.sleep(2)

        find_input = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
        find_input.send_keys(ACCOUNT)
        time.sleep(3)

        for _ in range(2):
            find_input.send_keys(Keys.ENTER)
            time.sleep(1)
        time.sleep(6)

        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(3)

    def follow(self, index=0):
        followers = self.driver.find_elements(By.CLASS_NAME, '_acan')
        i = index
        followers = followers[index:]
        for follower in followers:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView();", follower)
                time.sleep(1)
                i += 1
                follower.click()
                time.sleep(1)
                try:
                    cancel = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                    cancel.click()
                    time.sleep(1)
                except:
                    pass
            except:
                pass
            finally:

                self.follow(i)


Bot = InstagramFollowerBot()
Bot.login()
Bot.find_followers()
Bot.follow()
while True:
    pass