#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:18:50 2019

@author: abdullah
"""

def palindromity(string):
    '''
        time complexity ~ O(n)
    '''
    i, j = 0, len(string) - 1
    while i < j:
        while not string[i].isalnum() and i < j:
            i += 1
        while not string[j].isalnum() and i < j:
            j -= 1
        if string[i].lower() != string[j].lower():
            return False
        i, j = i + 1, j - 1
    return True