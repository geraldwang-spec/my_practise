#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:23:58 2026

@author: student
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import streamlit as st 
from selenium.webdriver.support.ui import WebDriverWait  #載入等待
from selenium.webdriver.support import expected_conditions as EC

#函數在此
def yahoo_search(keyword,pages):
    driver=webdriver.Chrome()  #C大寫
    driver.get('http://tw.search.yahoo.com')
    
    #進入等待, 超過10跳出
    wait=WebDriverWait(driver, 10)
    
    #找搜尋框
    box=wait.until(EC.presence_of_element_located((By.NAME,'p')))
    box.send_keys(keyword)
    box.send_keys(Keys.ENTER)
    
    time.sleep(2)
    
    results_all=[]
    for page in range(pages):
        
        
        #抓標題
        titles=driver.find_elements(By.CSS_SELECTOR,'h3 a')
        page_titles=[]
        
        for t in titles:
            text=t.text.strip()
            if text:
                page_titles.append(text)  #如果有抓到標題就接龍
        results_all.append((page+1,page_titles))        
    
        try:
            #找下一頁
            next_page=wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'下一頁')))
            next_page.click()              
            time.sleep(2)
        except:    
            print('找不到下一頁')
            break
        time.sleep(2)
    driver.quit()
    
    return results_all
    

st.title('yahoo 搜尋標題抓取器')
st.write('輸入關鍵字，選擇要抓幾頁, 按下按鈕開始搜尋')

keyword=st.text_input('請輸入搜尋關鍵字,',value='經典賽')
pages=st.slider('請選擇要搜尋幾頁',min_value=1,max_value=8,value=3,step=1)

if st.button('確認搜尋'):
    results= yahoo_search(keyword,pages)
    st.success('搜尋完成')
    
    for page_num,titles in results:
        st.subheader(f'第{page_num}頁')
        if titles:
            for i,title in enumerate(titles,start=1):
                st.write(f'{i}. {title}')   
        else:
            st.write('這一頁沒抓到標題')
