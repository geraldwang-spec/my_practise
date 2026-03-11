#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:45:54 2026

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

folder='momocatnew'
os.makedirs(folder,exist_ok=True)


driver=webdriver.Chrome()
driver.get('http://www.momoshop.com.tw')
print('已開啟momo')
wait = WebDriverWait(driver, 10)

box=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[type='text']")))
box.send_keys('cat')
time.sleep(2)
box.send_keys(Keys.ENTER)
time.sleep(2)

images=driver.find_elements(By.TAG_NAME, 'img')
print(f'picture count = {len(images)}')

img_urls = []
for img in images:
    src = img.get_attribute('src')
    if src and src.startswith('http'):
        img_urls.append(src)
        
print(f'valid picture http = {len(img_urls)}')

i = 1
for url in img_urls:
    if i>20:
        break;
    img_data = requests.get(url).content
    fname=f'cat{i}.jpg'
    fpath=os.path.join(folder,fname)
    with open(fpath,'wb') as f:
        f.write(img_data)
        
    print(f'downloading {fpath}')
    i+=1
driver.quit()