from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()

options.add_argument(r"user-data-dir=C:\Users\Shashwat Singh\AppData\Local\Microsoft\Edge\User Data")
options.add_argument("profile-directory=Profile 1")
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options = options)

x = 0
string = "qwertyuiopasdfghjklzxcvbnmqwerqwer"

while(x<34):
    string = string[:-1]
    driver.get(r"https://www.bing.com/search?q="+string)
    x+=1