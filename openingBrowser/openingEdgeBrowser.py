from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_Service = Service("drivers/msedgedriver.exe")
driver = webdriver.Edge(service=edge_Service)
driver.get("http://www.google.co.in")