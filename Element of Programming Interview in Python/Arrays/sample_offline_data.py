#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:03:02 2019

@author: abdullah
"""

import random

def sample_offline_data(A, size):
    '''
        time complexity ~ O(size)
        space complexity ~ O(1)
    '''
    if len(A) != len(set(A)):
        raise Exception("Duplicates present in the list")
    for i in range(size):
        r = random.randint(i,len(A)-1)
        A[i], A[r] = A[r], A[i]
    return A[:size]