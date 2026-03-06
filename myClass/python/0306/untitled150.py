#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 21:13:05 2026

@author: student
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
url = 'https://www.bing.com/'
driver.get(url)

# name='q'
box = driver.find_element(By.NAME, 'q')
box.send_keys("明天幾度？？")
time.sleep(1)
box.send_keys(Keys.ENTER)
time.sleep(1)

first=driver.find_element(By.TAG_NAME, 'h2')
first.click()
time.sleep(2)