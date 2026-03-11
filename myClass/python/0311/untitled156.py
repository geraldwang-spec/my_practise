#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:54:32 2026

@author: student
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait  #載入等待
from selenium.webdriver.support import expected_conditions as EC
import time


driver=webdriver.Chrome()  #C大寫
driver.get('http://tw.search.yahoo.com')

#進入等待, 超過10跳出
wait=WebDriverWait(driver, 10)

#找搜尋框
box=wait.until(EC.presence_of_element_located((By.NAME,'p')))
box.send_keys('經典賽')
box.send_keys(Keys.ENTER)


for page in range(3):
    print(f"----------page {page}--------")
    #wait=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3 a')))
    results = driver.find_elements(By.CSS_SELECTOR, 'h3 a')

    for i, r in enumerate(results, start = 5):
        text=r.text.strip()
        if text:
            print(f'{i}, {text}')
            
    time.sleep(2)
    
    try:
        next_page=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'下一頁')))
        next_page.click()
    except:
        print('找不到下一頁')
        break
    time.sleep(2)

#driver.quit()
        