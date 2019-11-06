#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:10:22 2019

@author: abdullah
"""

def combinations(n,k):
    """
        input: n - denoting an array [1,...,n] and k - size of subsets to return
        output: all subsets of size k
        
        time complexity ~ O(n x (n choose k))
    """
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(list(partial_combination))
            return
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i+1, partial_combination + [i])
            i += 1
            
    result = []
    directed_combinations(1,[])
    return result
