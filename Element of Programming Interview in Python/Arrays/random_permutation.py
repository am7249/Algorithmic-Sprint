#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:05:44 2019

@author: abdullah
"""

from sample_offline_data import sample_offline_data

def random_permutation(n):
    '''
        time complexity ~ O(n)
        space complexity ~ O(1)
    '''
    perm = list(range(n))
    sample_offline_data(perm,n)
    return perm
