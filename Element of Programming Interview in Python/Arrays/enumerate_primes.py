#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:58:25 2019

@author: macbook
"""

def primes(n):
    '''
        time complexity ~ O(nlog(log(n)))
        space complexity ~ O(n)
    '''
    count = [False, False] + [True]*(n-1)
    prime = []
    
    for p in range(2, n+1):
        if count[p]:
            prime.append(p)
            for i in range(p, n+1, p):
                count[i] = False
    return prime