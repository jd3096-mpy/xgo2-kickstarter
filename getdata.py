from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

import time
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.kickstarter.com/projects/xgorobot/xgo-2-worlds-first-raspberry-pi-robotic-dog-with-an-arm?ref=discovery')
time.sleep(5)
