import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select

fireFox_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=fireFox_Service)
driver.get("https://the-internet.herokuapp.com/dropdown")
options = Select(driver.find_element(By.ID,"dropdown"))

# Select By Value
options.select_by_value("2")

time.sleep(3)

#Select By Visible Text
options.select_by_visible_text("Option 1")
driver.close()

