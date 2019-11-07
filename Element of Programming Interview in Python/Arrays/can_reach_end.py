#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:50:31 2019

@author: macbook
"""

def can_reach_end(A):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    furthest, end_index = 0, len(A)-1
    i = 0
    min_steps = 0
    
    while i <= furthest and furthest < end_index:
        new_furthest = max(furthest, A[i] + i)
        if new_furthest != furthest:
            min_steps += 1
        furthest = new_furthest
        i += 1
    if furthest >= end_index:
        return True, min_steps
    else:
        return False