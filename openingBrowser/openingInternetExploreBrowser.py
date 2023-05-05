from selenium import webdriver
from selenium.webdriver.ie.service import Service

iE_Service = Service("drivers/IEDriverServer.exe")
driver = webdriver.Ie(service=iE_Service)
driver.get("http://www.google.co.in")

