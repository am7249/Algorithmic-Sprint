#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:51:04 2019

@author: abdullah
"""

def remove_duplicates_2(A):
    if not A:
        return 0
    
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index