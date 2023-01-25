from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

import time
from selenium import webdriver
driver = webdriver.Edge()
driver.get('https://www.kickstarter.com/projects/xgorobot/xgo-2-worlds-first-raspberry-pi-robotic-dog-with-an-arm?ref=discovery')
time.sleep(5)
