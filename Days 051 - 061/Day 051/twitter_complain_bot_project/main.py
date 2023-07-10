from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

SPEED_TEST_SITE = os.environ.get("SPEED_TEST_SITE")
TWITTER_SITE = os.environ.get("TWITTER_SITE")
TW_EMAIL = os.environ.get("TW_EMAIL")
TW_PASSWORD = os.environ.get("TW_PASSWORD")
TW_USERNAME = os.environ.get("TW_USERNAME")
PROMISED_DOW = 750
PROMISED_UP = 40

driver = webdriver.Chrome()


class InternetSpeedTwitterBot:
    def __init__(self):
        self.base_window = driver.window_handles[0]
        self.down = PROMISED_DOW
        self.up = PROMISED_UP
        self.speed_down, self.speed_up = 0, 0

    def get_internet_speed(self):
        driver.get(SPEED_TEST_SITE)
        driver.maximize_window()
        time.sleep(3)

        accept = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]')
        accept.click()
        time.sleep(3)

        start = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        time.sleep(40)

        self.speed_down = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.speed_up = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        time.sleep(3)
        return self.speed_down, self.speed_up

    def tweet_at_provider(self, down, up):
        driver.get(TWITTER_SITE)
        driver.maximize_window()
        time.sleep(3)

        email = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TW_EMAIL)
        continue_login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        continue_login.click()
        time.sleep(1)

        try:
            username = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys(TW_USERNAME)
            continue_login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
            continue_login.click()
            time.sleep(1)
        except:
            pass

        password = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TW_PASSWORD)
        login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login.click()
        time.sleep(10)

        message = f"Hey Internet Provider, why is my internet speed {down}down/{up}up when I pay for {self.down}down/{self.up}up?"
        try:
            input_tweet = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
            input_tweet.click()
            time.sleep(1)
            input_tweet = driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-ltr')
            input_tweet.send_keys(message)
        except:
            pass

        tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()


Bot = InternetSpeedTwitterBot()
speed_down, speed_up = Bot.get_internet_speed()
Bot.tweet_at_provider(speed_down, speed_up)
driver.quit()