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
driver.find_element(By.CSS_SELECTOR,"a[href = '#OKTab']").click()

driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-danger']").click()
alt = Alert(driver)
#Accept
alt.accept()

