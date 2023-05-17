import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

mozila_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=mozila_Service)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Click Here").click()

#prints the window handle in focus
print(driver.current_window_handle)

#to fetch the first child window handle
chwnd = driver.window_handles[1]

#to switch focus the first child window handle
driver.switch_to.window(chwnd)
time.sleep(5)
print(driver.find_element(By.TAG_NAME, "h3").text)
#to close the browser
driver.quit()