#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:55:27 2026

@author: student
"""
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


st.title('bing search')
keyword=st.text_input('please input keyword?')

if st.button('搜尋'):
 
    #driver=webdriver.Chrome('')
    
    #url='https://www.google.com/?hl=zh_TW'
    #url2='https://tw.yahoo.com'
    #url2='https://www.bing.com/'
    #driver 就是自動網頁
    #driver.get(url2)
    
    #box=driver.find_element(By.NAME,'p')
    #box.send_keys('明天幾度')
    #time.sleep(3)
    
    #box.send_keys(Keys.ENTER)
    #time.sleep(3)
    
    #titles=driver.find_elements(By.CSS_SELECTOR,'h3.title a')
    
    #for t in titles:
    #    print(t.text.split('\n')[-1])
        
    driver=webdriver.Chrome()
    url = 'https://www.bing.com/'
    driver.get(url)

    # name='q'
    box = driver.find_element(By.NAME, 'q')
    box.send_keys("明天幾度？？")
    time.sleep(1)
    box.send_keys(Keys.ENTER)
    time.sleep(1)
    
    titles=driver.find_elements(By.CSS_SELECTOR,'h2 a')
    for t in titles:
        st.write(t.text)
    
    #往下捲動
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #time.sleep(5)
    #for i in range(10):
    #    driver.execute_script("window.scrollBy(0,300)")
    #    time.sleep(0.5)

