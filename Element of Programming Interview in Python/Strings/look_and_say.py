#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:21:00 2019

@author: abdullah
"""

def look_and_say(n):
    '''
        time complexity ~ O(n x 2^n)
    '''
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return "".join(result)
    
    s = "1"
    for _ in range(n):
        s = next_number(s)
    return s