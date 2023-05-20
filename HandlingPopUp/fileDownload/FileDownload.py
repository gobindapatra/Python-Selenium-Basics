import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


mozilla_Service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=mozilla_Service)
driver.implicitly_wait(20)
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"LambdaTest.txt").click()
time.sleep(5)
