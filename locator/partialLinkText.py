from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

firefox_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=firefox_Service)
driver.get("https://www.redbus.in/")
driver.find_element(By.PARTIAL_LINK_TEXT, "About us").click()
driver.close()