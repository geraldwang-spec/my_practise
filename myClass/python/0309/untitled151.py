#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome('')

url='https://www.google.com/?hl=zh_TW'
#url2='https://tw.yahoo.com'
url2='https://www.bing.com/'
#driver 就是自動網頁
driver.get(url2)

#box=driver.find_element(By.NAME,'p')
#box.send_keys('明天幾度')
#time.sleep(3)

#box.send_keys(Keys.ENTER)
#time.sleep(3)

#titles=driver.find_elements(By.CSS_SELECTOR,'h3.title a')

#for t in titles:
#    print(t.text.split('\n')[-1])
    
#往下捲動
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
for i in range(10):
    driver.execute_script("window.scrollBy(0,300)")
    time.sleep(0.5)

