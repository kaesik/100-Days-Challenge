from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# driver.get("https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
# price = driver.find_element(By.CLASS_NAME, "priceToPay")
# print(price.text)

driver.get("https://www.python.org/")
# search = driver.find_element(By.NAME, "q")
# print(search.get_attribute("placeholder"))

# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)

link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(link.text)

driver.quit()
