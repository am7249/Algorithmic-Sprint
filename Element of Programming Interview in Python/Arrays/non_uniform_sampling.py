#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:13:58 2019

@author: macbook
"""

import itertools
import bisect
import random

def non_uniform_sampling(values, probabilities):
    '''
        time complexity ~ O(n)
        space complexity ~ O(n)
    '''
    partitions = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(partitions, random.random())
    return values[interval_idx]