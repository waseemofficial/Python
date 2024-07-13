from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("https://trytestingthis.netlify.app/")
first_name = driver.find_element(By.ID, "fname")
print(first_name.is_displayed())
print(first_name.is_enabled())
first_name.send_keys("FirstName")
last_name = driver.find_element(By.ID, "lname")
print(first_name.is_displayed())
print(first_name.is_enabled())
last_name.send_keys("LastName")
male = driver.find_element(By.ID, "male")
print(male.is_selected())

print(first_name.get_attribute("value"))
assert "F" in first_name.get_attribute("value")
print("radial button", male.get_attribute("value"))
time.sleep(10)
driver.close()
