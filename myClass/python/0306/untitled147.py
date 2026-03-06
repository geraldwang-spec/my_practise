#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 18:58:48 2026

@author: student
"""

import requests
import time
from bs4 import BeautifulSoup

headers={'User-Agent' : "Mozilla/5.0"}
pages = 2
for page in range(1, pages+1):
    url = f'https://ithelp.ithome.com.tw/?page={page}'
    
    r=requests.get(url, headers=headers)
    print('目前在第', page, '頁')
    
    soup=BeautifulSoup(r.text, 'html.parser')
    titles=soup.select('a.qa-list__title-link')
    counts=soup.select('span.qa-condition__count')
    view=counts[2].get_text(strip=True)
    
    for t in titles:
        print(t.get_text(strip=True))
    
        
    print('---------------------')
    time.sleep(1)