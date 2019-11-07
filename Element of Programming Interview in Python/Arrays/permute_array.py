#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:00:10 2019

@author: abdullah
"""

def permutations(A,P):
    """
    time complexity = O(n)
    space complexity = O(n)
    """
    perm = [0] * len(A)
    for i in range(len(A)):
        perm[P[i]] = A[i]
    return perm

def permutation_2(A, perm):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [a + len(perm) for a in perm]