import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:/Program Files/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
addToCartButtons = driver.find_elements(By.XPATH, "//div[@class='products']/div")

count = len(addToCartButtons)
assert count > 0
for addToCart in addToCartButtons:
    addToCart.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[contains(.,'PROCEED TO CHECKOUT')]").click()

driver.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulShetty")
driver.find_element(By.XPATH, "//button[@class='promoBtn']").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
print(driver.find_element(By.XPATH, "//span[@class='promoInfo']").text)


