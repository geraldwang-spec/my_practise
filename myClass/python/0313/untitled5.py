#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:49:23 2026

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
from PIL import Image

st.title('圖片搜尋與展示')
folder = 'momonew'


keyword=st.text_input('請輸入關鍵字', 'cat')
folder=st.text_input('圖片folder','momonew')
os.makedirs(folder, exist_ok=True)
col_nums = st.slider('一排顯示的張數', 2, 6, 2)
min_size=st.slider('過瀘圖片大小(最小寬高)', 50, 800, 200)

if st.button('開始下載圖片'):
    st.success('準備下載…')
    driver=webdriver.Chrome()  
    driver.get('https://www.momoshop.com.tw')
    print('已開啟 momo')
    #進入等待, 超過10跳出
    wait=WebDriverWait(driver, 10)    

    #找搜尋框用  html的語法來定位搜尋欄位
    box=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='text']")))

    #輸入文字來搜尋圖片
    box.send_keys(keyword)
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
        if i >50:
            break
        img_data=requests.get(url, verify=False).content  #數位內容　加上verify=False
        fname=f'cat0{i}.jpg'
        #學會寫路徑
        fpath=os.path.join(folder,fname)    
        with open(fpath,'wb') as f:
            f.write(img_data)
        
        print(f'已下載 {fpath}')
        i += 1   #i=i+1
    driver.quit()
    
files=os.listdir(folder)

image_files = [f for f in files if f.endswith(('.jpg','.png','.jpeg'))]
cols = st.columns(col_nums)

i = 0
for f in image_files:
    path=os.path.join(folder, f)
    with cols[i % col_nums]:
        img = Image.open(path)
        w,h = img.size
        if w>=min_size and h >=min_size:
            st.image(path,width=200)
            st.caption(f'{f} ({w}x{h})')
            i += 1