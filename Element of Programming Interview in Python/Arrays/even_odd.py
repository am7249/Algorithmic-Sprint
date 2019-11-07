#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:44:34 2019

@author: abdullah
"""

def even_odd(A):
    """take advantage of the fact that you can operate on both ends
    effectively. Partition the array into Even, Unclassified, and Odd.
    Initially Even and Odd are empty, we iterate through the Unclassified
    and keep filling Even and Odd.
    
    O(n) time complexity and O(1) space complexity"""
    
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A