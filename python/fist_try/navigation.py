from http.server import executable
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import by
driver = webdriver.Firefox()
driver.get("https://trytestingthis.netlify.app/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.google.com")
print(driver.title)
print(driver.current_url)
driver.back()
print(driver.title)
print(driver.current_url)
driver.forward()
print(driver.title)
print(driver.current_url)

#a = driver.find_element(by.xpath("//*[@id='fname']"))
# print(a)
driver.close()
