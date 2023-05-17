import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

mozila_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=mozila_Service)
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"img[class='imgdp']").click()
for i in range(3):
    driver.find_element(By.CSS_SELECTOR, "a[title='Next']").click()
driver.find_element(By.LINK_TEXT, "3").click()

