#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:36:49 2026

@author: student
"""

from selenium import webdriver

driver1=webdriver.Chrome()
url1='https://www.google.com/'
driver1.get(url1)

driver2=webdriver.Chrome()
url2='https://ithelp.ithome.com.tw/'
driver2.get(url2)

driver3=webdriver.Chrome()
url3='https://tw.yahoo.com/'
driver3.get(url3)

print('注意工作列有沒有出現新的broser')