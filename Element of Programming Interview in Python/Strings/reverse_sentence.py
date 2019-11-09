#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:19:58 2019

@author: abdullah
"""

def reverse_sentence(sent):
    '''
        time complexity ~ O(n)
        space complexity ~ O(1)
    '''
    
    sent.reverse() #sent is a bytearray
    
    def reverse_word(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
            
    start = 0
    while True:
        end = sent.find(b' ', start)
        if end < 0:
            break
        reverse_word(sent, start, end - 1)
        start = end + 1
    reverse_word(sent, start, len(sent) - 1)
    return sent