#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:04:38 2019

@author: abdullah
"""

def permutations(A):
    """
        input: an array
        output: all the permutations of the input array
        
        time complexity ~ O(n x n!)
    """
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutations(i+1)
            A[i], A[j] = A[j], A[i]
    result = []
    directed_permutations(0)
    return result