#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:47:23 2026

@author: student
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
url = 'https://www.google.com/'
driver.get(url)
# name="q"
#希望把搜尋填入，google的空位
box = driver.find_element(By.NAME, 'q')
box.send_keys("明天幾度？？")
time.sleep(1)
box.send_keys(Keys.ENTER)
