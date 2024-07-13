from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("https://trytestingthis.netlify.app/index.html")
user_name = driver.find_element(By.ID, "uname")
password = driver.find_element(By.ID, "pwd")
user_name.send_keys("test")
password.send_keys("test")
driver.find_element(By.XPATH, "(//input[@value='Login'])[1]").click()
time.sleep(2)
print(driver.title)
assert "Login Success" in driver.title
time.sleep(2)
driver.find_element(By.LINK_TEXT, "here").click()
print(driver.current_url)
assert "https://trytestingthis.netlify.app/index.html" in driver.current_url
time.sleep(2)

driver.close()
