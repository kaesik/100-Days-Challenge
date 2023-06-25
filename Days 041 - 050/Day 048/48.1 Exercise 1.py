from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

menu = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')

dates = [f"2023-{date.text}" for date in menu.find_elements(By.TAG_NAME, "time")]
events = [event.text for event in menu.find_elements(By.TAG_NAME, "a")]

dates_events = {date: event for date, event in zip(dates, events)}
events_dict = {}

for index, element in enumerate(dates_events):
    date_event = {element: dates_events[element]}
    events_dict[index] = date_event

print(events_dict)

driver.quit()
