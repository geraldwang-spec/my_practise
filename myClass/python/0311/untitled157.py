#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 19:39:17 2026

@author: student
"""

import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait  #載入等待
from selenium.webdriver.support import expected_conditions as EC
import time


def yahoo_search(keyword, pages):
    driver=webdriver.Chrome()  #C大寫
    driver.get('http://tw.search.yahoo.com')

    #進入等待, 超過10跳出
    wait=WebDriverWait(driver, 10)

    #找搜尋框
    box=wait.until(EC.presence_of_element_located((By.NAME,'p')))
    box.send_keys(keyword)
    box.send_keys(Keys.ENTER)
    
    time.sleep(2)
    results_all = []
    for page in range(pages):
        #wait=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3 a')))
        titles = driver.find_elements(By.CSS_SELECTOR, 'h3 a')
        page_titles=[]
        
        for t in titles:
            text=t.text.strip()
            if text:
                page_titles.append(text)
                
        results_all.append((page+1, page_titles))
        try:
            next_page = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, '下一頁')))
            next_page.click()
            time.sleep(2)
        except:
            print('找不到下一頁')
            break
        time.sleep(2)
    driver.quit()
    return results_all

st.title('yahoo search ')
st.write('input key word, how many pages, click search button')
keyword = st.text_input('Please input key word', value='經典賽')
pages=st.slider('how many page', min_value=1, max_value=8, value=3,step=1)
if st.button('search'):
    results=yahoo_search(keyword,pages)
    st.success('search ready')
    
    for page_num, titles in results:
        st.subheader(f'{page_num}')
        if titles:
            for i, title in enumerate(titles,start=1):
                st.write(f"{i} {title}")
        else:
           st.write('ddd')

    

    