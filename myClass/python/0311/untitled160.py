#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 21:40:46 2026

@author: student
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait  #載入等待
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

#建立資料夾
folder='momocatnew'
os.makedirs(folder,exist_ok=True)

driver=webdriver.Chrome()  #C大寫
driver.get('https://www.momoshop.com.tw')
print('已開啟 momo')
#進入等待, 超過10跳出
wait=WebDriverWait(driver, 10)    

#找搜尋框用  html的語法來定位搜尋欄位
box=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='text']")))

#輸入文字來搜尋圖片
box.send_keys('cat')
time.sleep(2)
box.send_keys(Keys.ENTER)
time.sleep(2)

#抓照片  img src
images=driver.find_elements(By.TAG_NAME,'img')
print(f'抓到圖片的數量:{len(images)}')

#收集照片的網址來下載
img_urls=[]

for img in images:
    src=img.get_attribute('src')
    if src and src.startswith('http'):
        img_urls.append(src)
print(f'有效圖片的數量:{len(img_urls)}')

#下載前20張圖片
i= 1
for url in img_urls:
    if i >20:
        break
    img_data=requests.get(url, verify=False).content  #數位內容
    fname=f'cat0{i}.jpg'
    #學會寫路徑
    fpath=os.path.join(folder,fname)    
    with open(fpath,'wb') as f:
        f.write(img_data)
    
    print(f'已下載 {fpath}')
    i += 1   #i=i+1
driver.quit()
