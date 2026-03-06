#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:07:43 2026

@author: student
"""

from selenium import webdriver
import time

driver1=webdriver.Chrome()
url1='https://www.google.com/'
url2 =' https://tw.yahoo.com'
url3 = 'https://www.ptt.cc/bbs/nba/index.html'

#driver1.get(url1)

#driver1.execute_script("window.open('https://tw.yahoo.com');")
#driver1.execute_script("window.open('https://www.ptt.cc/bbs/nba/index.html);")

sites = [url1, url2, url3]
for s in sites:
    driver1.execute_script(f"window.open('{s}');")
    time.sleep(1)
