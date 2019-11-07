#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:49:08 2019

@author: abdullah
"""

def increment(A):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    
    #carry = False
    for i in range(len(A)-1,-1,-1):
        if A[i] + 1 <= 9:
            A[i] += 1
            break
        elif A[i] + 1 > 9:
            if i == 0:
                A[i] = 1
                A.append(0)
            else:
                A[i] = 0
    return A