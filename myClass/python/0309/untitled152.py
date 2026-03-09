#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:42:37 2026

@author: student
"""

import streamlit as st
st.title('我的第一個st網站')
name=st.text_input('請輸入你的名字??')
st.write('你好', name)