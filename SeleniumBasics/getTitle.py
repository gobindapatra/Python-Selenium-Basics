from selenium import webdriver
from selenium.webdriver.firefox.service import Service

firefox_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=firefox_Service)
driver.get("https://www.redbus.in/")
print (driver.title)
driver.close()