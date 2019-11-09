#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:16:10 2019

@author: abdullah
"""

import functools

def ss_decode_col_id(col):
    return functools.reduce(
            lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)