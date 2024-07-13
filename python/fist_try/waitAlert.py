from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Firefox()
driver.get("https://trytestingthis.netlify.app/index.html")
driver.implicitly_wait(10)  # time in seconds
allert = driver.find_element(
    By.XPATH, "//button[normalize-space()='Your Sample Alert Button!']")
allert.click()
time.sleep(10)
print(driver.switch_to.alert.text)
alert_box = driver.switch_to.alert
alert_box.accept()
conf = driver.find_element(
    By.XPATH, "//div[@class='pop-up-alert']//p[@id='demo']")
assert "You Pressed the OK Button!" in conf.text


print(conf.text)

driver.close()
