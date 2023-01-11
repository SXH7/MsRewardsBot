from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()

mobile_emulation = {
     "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
     "userAgent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78"
}

options.add_argument(r"user-data-dir=C:\Users\Shashwat Singh\AppData\Local\Microsoft\Edge\User Data")
options.add_argument("profile-directory=Profile 1")
options.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options = options)

x = 0
string = "aqwertyuiopasdfghjklzxcvbnmqwerqwer"

while(x<35):
    string = string[:-1]
    driver.get(r"https://www.bing.com/search?q="+string)
    x+=1

driver.close()

options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Edge(options = options)

stringmob = "mnbvcxzlkjhgfdsapoiut"
x=0
while(x<21):
    driver.get(r"https://www.bing.com/search?q="+stringmob)
    x+=1
    stringmob = stringmob[:-1]
    time.sleep(1)