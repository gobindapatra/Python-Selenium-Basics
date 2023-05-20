import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

mozila_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=mozila_Service)
driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()
createAccount = driver.find_element(By.LINK_TEXT, "Create an Account")
time.sleep(2)
GearElement = driver.find_element(By.XPATH, "//a[@id='ui-id-6']")

#Click
ActionChains(driver).click(createAccount).perform()

#Context Click
ActionChains(driver).context_click(GearElement).perform()

#Click and hold
ActionChains(driver).click_and_hold(GearElement).perform()

#Double click
ActionChains(driver).double_click(GearElement).perform()

#Move to element
ActionChains(driver).move_to_element(GearElement).perform()

