from selenium import webdriver
from selenium.webdriver.firefox.service import Service

firefox_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=firefox_Service)
driver.get("http://www.google.co.in")


# close  windows that current pointing
#driver.quit()

# close all windows
driver.close()


