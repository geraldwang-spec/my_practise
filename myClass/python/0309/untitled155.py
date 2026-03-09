#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:14:30 2026

@author: student
"""

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
     with st.spinner('正在搜尋並捲動頁面…'):
        driver=webdriver.Chrome()
        url = 'https://www.bing.com/'
        driver.get(url)
    
        # name='q'
        box = driver.find_element(By.NAME, 'q')
        box.send_keys(keyword)
        time.sleep(1)
        box.send_keys(Keys.ENTER)
        time.sleep(1)
        
        for i in range(10):
            driver.execute_script("window.scrollBy(0,300)")
            time.sleep(0.5)
        
        titles=driver.find_elements(By.CSS_SELECTOR,'h2 a')
        for t in titles:
            st.write(t.text)

        driver.quit()
