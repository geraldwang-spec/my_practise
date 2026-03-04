#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 18:45:05 2026

@author: student
"""
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
}

url = 'https://www.google.com/?hl=zh_TW'
url2 = 'https://tw.yahoo.com/'
url3 = 'https://www.amazon.com/'
re=requests.get(url, headers=headers)
print(re)
re2=requests.get(url2, headers=headers)
print(re2)
re3=requests.get(url3, headers=headers)
print(re3)


