#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 10:54:55 2019

@author: abdullah
"""

def buy_sell_stocks_2(A):
    '''
        time complexity ~ O(n)
        space complexity ~ O(1)
    '''
    
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in A:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit