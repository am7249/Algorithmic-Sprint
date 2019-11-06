#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:16:02 2019

@author: abdullah
"""

def palindromic_decompositions(input_string):
    """
        input: a string
        output: all palindromic decompositions of the input string
        
        time complexity ~ O(n x 2^n)
    """
    def directed_palindromic_decomposition(offset, decomp):
        if offset == len(input_string):
            result.append(list(decomp))
            return 
        for i in range(offset+1,len(input_string)+1):
            prefix = input_string[offset:i]
            if prefix == prefix[::-1]:
                directed_palindromic_decomposition(i, decomp+[prefix])
    result = []
    directed_palindromic_decomposition(0,[])
    return result