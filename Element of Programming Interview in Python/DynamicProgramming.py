#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 14:30:41 2019

@author: macbook
"""

import itertools

def fibonacci_DP(n, cache={}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci_DP(n-1) + fibonacci_DP(n-2)
    return cache[n]

def fibonacci_2(n):
    if n <= 1:
        return n
    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1,n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f

def maximum_subarray(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum

def score_combination(n,points): 
  
    # table[i] will store count of solutions for value i. 
    # Initialize all table values as 0. 
    table = [0 for i in range(n+1)] 
  
    # Base case (If given value is 0) 
    table[0] = 1
  
    for point in points:
        for i in range(point, n+1): 
            table[i] += table[i-point] 
  
    return table[n]


#print(score_combination(50,[3,5,10]))
#print(maximum_subarray([1,2,3,4,5,1,-3,17,-30]))
#print(fibonacci_2(20))