from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")
LINKEDIN_SITE = os.environ.get("LINKEDIN_SITE")

driver = webdriver.Chrome()
driver.get(LINKEDIN_SITE)
driver.maximize_window()


def accept_cookies():
    accept = driver.find_element(By.CLASS_NAME, "artdeco-global-alert-action")
    accept.click()


def login():
    login = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
    login.click()
    time.sleep(2)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    login_again = driver.find_element(By.CLASS_NAME, "btn__primary--large")

    username.send_keys("kaes100day@gmail.com")
    password.send_keys(LINKEDIN_PASSWORD)
    login_again.click()


def look_for_job(index):
    jobs = driver.find_elements(By.CLASS_NAME, "artdeco-entity-lockup__title")
    i = index
    jobs = jobs[index:]
    try:
        for job in jobs:
            try:
                driver.execute_script("arguments[0].scrollIntoView();", job)
                time.sleep(1)
            except:
                pass
            finally:
                job.click()
                time.sleep(1)
                save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
                save.click()
                time.sleep(1)
                i += 1
    except:
        pass
    look_for_job(i)


time.sleep(1)
accept_cookies()
time.sleep(1)
login()
time.sleep(1)
look_for_job(0)
while True:
    pass