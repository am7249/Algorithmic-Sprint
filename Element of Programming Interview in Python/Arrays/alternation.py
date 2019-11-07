#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:56:52 2019

@author: abdullah
"""

def alternation(A):
    '''
        time complexity ~ O(n)
        space complexity ~ O(1)
    '''
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2)
    return A