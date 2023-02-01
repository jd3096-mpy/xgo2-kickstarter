import time

# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# 
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# 
# time.sleep(1)
print('driver installed')
#------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
desired_capabilities = DesiredCapabilities.EDGE
desired_capabilities["pageLoadStrategy"] = "none"


driver = webdriver.Edge()
print(0)
driver.get('https://www.kickstarter.com/projects/xgorobot/xgo-2-worlds-first-raspberry-pi-robotic-dog-with-an-arm?ref=discovery')
print(1)
time.sleep(10)
print(2)
money_data=driver.find_element(By.XPATH, '//*[@id="react-project-header"]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/span/span')
people_data=money=driver.find_element(By.XPATH, '//*[@id="react-project-header"]/div/div[1]/div[3]/div/div[2]/div[2]/div/span')
money=re.findall("\d+",money_data.text) 
people=re.findall("\d+",people_data.text) 
people=people[0]
print(people)
mm=''
for m in money:
    mm+=str(m)
money=int(mm)
print(money)


import requests
import json
headers={"api-key":"VqL9j56HfXisdr8nOvGT=iLl95g="}
url='http://api.heclouds.com/devices/1039865113/datapoints'
payload = {'datastreams': [{"id": "followers", "datapoints": [{"value": int(people)}]}]}
payload=json.dumps(payload)
ok=requests.post(headers=headers,url=url,data=payload)
print(ok.text)

payload = {'datastreams': [{"id": "moneys", "datapoints": [{"value": int(people)}]}]}
payload=json.dumps(payload)
ok=requests.post(headers=headers,url=url,data=payload)
print(ok.text)

driver.close()


