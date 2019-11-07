#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:45:41 2019

@author: abdullah
"""

def dutch_flag_1(A, i):
    """
    time complexity = O(n)
    space complexity = O(n)    
    """
    _A = []
    pivot = A[i]
    for elem in A:
        if elem < pivot:
            _A.append(elem)
    for elem in A:
        if elem == pivot:
            _A.append(elem)
    for elem in A:
        if elem > pivot:
            _A.append(elem)
    
    return _A

def dutch_flag_2(A, i):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    l, p1, g = 0, 0, len(A) - 1
    pivot = A[i]
    
    while p1 < g:
        if A[p1] < pivot:
            A[l], A[p1] = A[p1], A[l]
            l, p1 = l + 1, p1 + 1
        elif A[p1] == pivot:
            p1 += 1
        else:
            g -= 1
            A[p1], A[g] = A[g], A[p1]
    return A