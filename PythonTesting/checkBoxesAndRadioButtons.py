import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Program Files/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if (checkbox.get_attribute("value")) == "option3":
        assert not checkbox.is_selected()
        checkbox.click()
        assert checkbox.is_selected()
        break
time.sleep(5)

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected()
