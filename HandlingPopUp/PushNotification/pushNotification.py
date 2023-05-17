import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get("https://chercher.tech/practice/hidden-division-popup")
time.sleep(5)

