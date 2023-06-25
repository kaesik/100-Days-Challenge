from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Kamil")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Sobania")

email = driver.find_element(By.NAME, "email")
email.send_keys("kamil.sobania.97@gmail.com")

button = driver.find_element(By.TAG_NAME, "button")
button.click()

while(True):
    pass