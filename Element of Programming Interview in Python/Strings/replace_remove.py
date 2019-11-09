#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:17:47 2019

@author: abdullah
"""

def replace_and_remove(size, s):
    '''
        time complexity ~ O(n)
        space complexity ~ O(1)
    '''
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
    
    curr_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    
    while curr_idx >= 0:
        if s[curr_idx] == 'a':
            s[write_idx - 1 : write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1
    return final_size