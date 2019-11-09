#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:10:56 2019

@author: abdullah
"""

def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
        
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    
    return ('-' if is_negative else '') + ''.join(reversed(s))