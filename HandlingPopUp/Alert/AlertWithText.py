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
driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[class ='btn btn-info']").click()
alt = Alert(driver)

#Get Message displayed in alert
message =alt.text
print(message)

#send input to Alert
alt.send_keys("automation user")

#cancel the alert
alt.dismiss()

