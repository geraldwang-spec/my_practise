#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:09:01 2026

@author: student
"""

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}

url = "https://www.ptt.cc/bbs/nba/index.html"
re = requests.get(url)
print(re)

soup = BeautifulSoup(re.text, 'lxml')
print(soup.prettify())

#soup = BeautifulSoup(re.text, 'html.parser')
#print(soup.prettify())

#class="title" 保留字不能用，請加底線
title=soup.find_all('div', class_='title')

for t in title:
    print(t.text)
    
authors = soup.find_all('div', class_='author')
for a in authors:
    print(a.text)
    
#CSS選擇器  class="r-ent" , 選擇器的上下階層是用 . 隔開
posts=soup.select('div.r-ent') 
print('抓到的文章數',len(posts))   
'''
for p in posts:
    nrec_tag=p.select_one('.nrec span')
    nrec=nrec_tag.get_text(strip=True) if nrec_tag else '0'
        
    print(nrec)

# A if 條件 else B
#如果條件成立 ，回傳a 
#不成立就是b  

if nrec_tag:
    nrec=nrec_tag_text(strip=True)
else :
    nrec = '0'
'''




