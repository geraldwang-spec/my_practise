# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup

print('OK')

# read local html file
with open('a12.html' , 'r', encoding='utf-8') as f:
    html=f.read()
    
# analysis
soup = BeautifulSoup(html, 'html.parser')

# get src of all picture
for img in soup.find_all('img'):
    print("found")
    print(img.get('src'))
    
# get our web css context
style_tag = soup.find("style")
print(style_tag.text)
print(style_tag.text)