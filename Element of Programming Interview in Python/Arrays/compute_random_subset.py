#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:12:26 2019

@author: abdullah
"""

import random

def random_subset(n, k):
    '''
        time complexity ~ O(k)
        space complexity ~ O(k)
    '''
    change_ind = {}
    for i in range(k):
        rand_idx = random.randrange(i,n)
        rand_idx_mapped = change_ind.get(rand_idx,rand_idx)
        i_mapped = change_ind.get(i, i)
        change_ind[rand_idx] =  i_mapped
        change_ind[i] = rand_idx_mapped
    return [change_ind[i] for i in range(k)]
