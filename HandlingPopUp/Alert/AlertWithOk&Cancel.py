import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

mozila_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=mozila_Service)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Alert with OK & Cancel").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
alt = Alert(driver)

#ok
alt.accept()

#cancel
alt.dismiss()

