#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 18:57:26 2026

@author: student
"""
import streamlit as st
import os
from PIL import Image

st.title('圖片展示')

folder='aaa'  #要檢視的照片的目錄

files=os.listdir(folder)

image_files = [f for f in files if f.endswith(('.jpg','.png','.jpeg'))]


# control column counts
colcount=st.slider('picture counts', min_value=2, max_value=6, value=2,step=1)
# control picture size
min_size=st.slider('過濾圖片大小(最小寬高)', 50, 800, 200)

cols = st.columns(colcount)

i = 0
for f in image_files:
    path=os.path.join(folder, f)
    with cols[i % colcount]:
        #st.image(path, caption=f)
            
        img = Image.open(path)
        w,h = img.size
        
        # filter picture
        if w>=min_size and h >=min_size:
            st.image(path,width=200)
            st.caption(f'{f} ({w}x{h})')
            i += 1
        
