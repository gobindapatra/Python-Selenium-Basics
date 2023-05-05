from selenium import webdriver
from selenium.webdriver.firefox.service import Service

firefox_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=firefox_Service)
driver.get("http://www.google.co.in")

#maximize winodow
driver.maximize_window()

#minimize winodow
driver.minimize_window()

driver.close()


