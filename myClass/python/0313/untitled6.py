#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:26:43 2026

@author: student
"""

from flask import Flask
app=Flask(__name__)

@app.route('/')

def home():
    return 'Hello Flask'

if __name__ == '__main__':
    app.run(debug=True)
