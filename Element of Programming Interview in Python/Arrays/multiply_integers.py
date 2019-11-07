#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:49:43 2019

@author: abdullah
"""

def multiply(A, B):
    """
    time complexity = O(nm)
    space complexity = O(n + m)
    """
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    A[0], B[0] = abs(A[0]), abs(B[0])
    
    result = [0] * (len(A) + len(B))
    
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            result[i + j + 1] += A[i] * B[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    result = result[next((i for i, x in enumerate(result)
                        if x != 0), len(result)):] or [0]
    
    return [sign * result[0]] + result[1:]
