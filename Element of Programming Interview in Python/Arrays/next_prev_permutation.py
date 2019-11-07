#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:01:01 2019

@author: abdullah
"""

def next_permutation(P):
    '''
        time complexity ~ O(n)
        space complexity ~ O(1)
    '''
    inversion_point = len(P) - 2
    while (inversion_point >= 0 and P[inversion_point] >= P[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []
    
    for i in reversed(range(inversion_point + 1, len(P))):
        if P[i] > P[inversion_point]:
            P[inversion_point], P[i] = P[i], P[inversion_point]
            break
    
    P[inversion_point + 1:] = reversed(P[inversion_point + 1:])
    return P



def prev_permutation(P):
    '''
        time complexity ~ O(n)
        space complexity ~ O(1)
    '''
    inversion_point = len(P) - 2
    while (inversion_point >= 0 and P[inversion_point] <= P[inversion_point+1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []
    
    for i in reversed(range(inversion_point + 1, len(P))):
        if P[i] < P[inversion_point]:
            P[inversion_point], P[i] = P[i], P[inversion_point]
            break
    P[inversion_point + 1:] = reversed(P[inversion_point + 1:])
    return P
