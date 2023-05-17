import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

mozila_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=mozila_Service)
driver.get("https://chercher.tech/practice/hidden-division-popup")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "a[class='cd-popup-trigger']").click()
driver.find_element(By.XPATH, "//input[.='']").send_keys("Aotomation Tester")
driver.find_element(By.CLASS_NAME, "alert").click()

