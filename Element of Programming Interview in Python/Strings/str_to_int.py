#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:12:26 2019

@author: abdullah
"""

import functools

def str_to_int(s):
    return functools.reduce(
            lambda running_sum, c: running_sum * 10 + s.index(c),
            s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)