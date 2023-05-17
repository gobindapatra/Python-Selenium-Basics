import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

mozilla_Service = Service("drivers/geckodriver.exe")
driver = webdriver.Firefox(service=mozilla_Service)
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://the-internet.herokuapp.com")
#to refresh the browser
driver.refresh()
driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT, "Nested Frames").click()

# to switch to frame with frame name
driver.switch_to.frame("frame-bottom")

# to get the text inside the frame and print on console
time.sleep(5)
print(driver.find_element(By.CSS_SELECTOR, "body").text)

# to move out the current frame to the page level
driver.switch_to.default_content()

#to close the browser
driver.quit()