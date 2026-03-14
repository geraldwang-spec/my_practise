#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 18:57:26 2026

@author: student
"""
import streamlit as st
import os

st.title('圖片展示')

folder='aaa'  #要檢視的照片的目錄

files=os.listdir(folder)

image_files = [f for f in files if f.endswith(('.jpg','.png','.jpeg'))]

#for f in files:
#    if f.endswith((('.jpg','.png','.jpeg'))):
#        path=os.path.join(folder,f)
#        st.image(path,caption=f)

colcount=st.slider('', min_value=2, max_value=6, value=2,step=1)

cols = st.columns(colcount)

i = 0
for f in image_files:
    path=os.path.join(folder, f)
    with cols[i%colcount]:
        st.image(path, caption=f)

    i+=1        

