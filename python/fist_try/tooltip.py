from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get("https://trytestingthis.netlify.app/")

tooltip = driver.find_element(By.CLASS_NAME, "tooltip")
print(tooltip.text)
actions = ActionChains(driver)
actions.move_to_element(tooltip)
actions.perform()
time.sleep(10)
tooltip_text = driver.find_element(By.CSS_SELECTOR, ".tooltiptext")
print(tooltip_text.text)
assert "This is your sample Tooltip text" in tooltip_text.text
driver.close()
