from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome_Service = Service("drivers/chromedriver.exe")
# driver = webdriver.Chrome(service=Chrome_Service)
driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
driver.get("http://www.google.co.in")
driver.close()