from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

SITE = os.environ.get("SITE")

driver = webdriver.Chrome()
driver.get(SITE)
driver.maximize_window()