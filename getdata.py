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

driver = webdriver.Edge()
driver.get('https://www.kickstarter.com/projects/xgorobot/xgo-2-worlds-first-raspberry-pi-robotic-dog-with-an-arm?ref=discovery')
time.sleep(50)
datas=driver.find_element(By.XPATH, '//*[@id="react-prelaunch-root"]/div/div/div/div/div[2]/div[1]/div[2]/span')
nums=re.findall("\d+",datas.text) 
people=nums[0]
print(people)
with open('result.txt','w') as f:
    f.write(people)

import requests
import json
headers={"api-key":"VqL9j56HfXisdr8nOvGT=iLl95g="}
url='http://api.heclouds.com/devices/1039865113/datapoints'
payload = {'datastreams': [{"id": "followers", "datapoints": [{"value": int(people)}]}]}
payload=json.dumps(payload)
ok=requests.post(headers=headers,url=url,data=payload)
print(ok.text)
driver.close()

