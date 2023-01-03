from selenium import webdriver
from selenium.webdriver.edge.options import Options

options = Options()

driver = webdriver.Edge(options = options)
driver.get(r"https://youtube.com")
