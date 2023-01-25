import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

time.sleep(1)
print('driver installed')
#------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

driver = webdriver.Edge()
driver.get('https://www.kickstarter.com/projects/xgorobot/xgo-2-worlds-first-raspberry-pi-robotic-dog-with-an-arm?ref=discovery')
time.sleep(5)
datas=driver.find_element(By.XPATH, '//*[@id="react-prelaunch-root"]/div/div/div/div/div[2]/div[1]/div[2]/span')
nums=re.findall("\d+",datas.text) 
people=nums[0]
print(people)
with open('result.txt','w') as f:
    f.write(people)
driver.close()

