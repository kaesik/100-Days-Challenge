from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import requests as rq
import time
import os

GOOGLE_DOC = os.environ.get("GOOGLE_DOC")
ZILLOW = os.environ.get("ZILLOW")
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

class ZillowBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_window = self.driver.window_handles[0]
        self.response = rq.get(ZILLOW, headers=HEADERS).text
        self.soup = BeautifulSoup(self.response, "html.parser")
        self.address = []
        self.price = []
        self.link = []


    def get_data(self):
        offers = self.soup.find("ul", class_="photo-cards").find_all("li")
        for offer in offers:
            try:
                address = offer.find("address").getText()
                price = offer.find("span").getText()
                link = f'https://www.zillow.com{offer.find("a").get("href").split("https://www.zillow.com")[1]}'
                self.address.append(address)
                self.price.append(price)
                self.link.append(link)
            except:
                pass

    def menage_data(self):
        self.driver.get(GOOGLE_DOC)
        self.driver.maximize_window()
        time.sleep(3)
        for i in range(len(self.address)):
            address_field = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
            address_field.send_keys(self.address[i])
            price_field.send_keys(self.price[i])
            link_field.send_keys(self.link[i])
            submit_button.click()
            time.sleep(2)

            self.driver.switch_to.window(self.base_window)
            time.sleep(2)

            self.driver.refresh()
            time.sleep(2)

Bot = ZillowBot()
Bot.get_data()
Bot.menage_data()

