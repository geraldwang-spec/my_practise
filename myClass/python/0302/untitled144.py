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


for p in posts:
    title_tag=p.select_one('.title a')
    author_tag=p.select_one('.author')
    nrec_tag=p.select_one('.nrec span')
    
    title=title_tag.get_text(strip=True) if title_tag else ""
    author = author_tag.get_text(strip=True) if author_tag else ""
    nrec = nrec_tag.get_text(strip=True) if nrec_tag else ""
    
    print(f'{nrec:>3} | {author:<12} | {title}')


'''
for p  in posts:
    
    #等待修改 
    title_tag=p.select_one('.title a')
    author_tag=p.select_one('.author') 
    nrec_tag=p.select_one('.nrec span') 
    
    
    title= title_tag.get_text(strip=True) if title_tag else "" 
    author= author_tag.get_text(strip=True) if author_tag else ""  
    nrec= nrec_tag.get_text(strip=True) if nrec_tag else ""  
        
    print(f'{nrec:>3}  |{author:<12} | {title} ')
'''

# <div class="btn-group btn-group-paging">
# <a class="btn wide" href="/bbs/NBA/index6502.html">‹ 上頁</a>
btns=soup.select('div.btn-group-paging a')
print(f' button count = {len(btns)}')

prev_url=None
for b in btns:
    if '上頁'  in b.text:
        prev_url = 'https://www.ptt.cc/' + b['href']
        
print("找到上頁網址是", prev_url)

if prev_url:
    re2 = requests.get(prev_url)
    soup2=BeautifulSoup(re2.text, 'lxml')
    posts2=soup2.select('div.r-ent') 
    print('抓到的文章數',len(posts))   

    for p in posts2:
        title_tag=p.select_one('.title a')
        author_tag=p.select_one('.author')
        nrec_tag=p.select_one('.nrec span')
        
        title=title_tag.get_text(strip=True) if title_tag else ""
        author = author_tag.get_text(strip=True) if author_tag else ""
        nrec = nrec_tag.get_text(strip=True) if nrec_tag else ""
        
        print(f'{nrec:>3} | {author:<12} | {title}')

