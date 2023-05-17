from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


mozilla_Service = Service("drivers/chromedriver.exe")
driver = webdriver.Chrome(service=mozilla_Service)
driver.implicitly_wait(20)
driver.get("https://the-internet.herokuapp.com/upload")
driver.find_element(By.ID, "file-upload").send_keys("selenium-snapshot.jpg")
driver.find_element(By.ID, "file-submit").submit()
if driver.page_source.find("File Uploaded!"):
    print("file upload success")
else:
    print("file upload not successful")
driver.quit()

