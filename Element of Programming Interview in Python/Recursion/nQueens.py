#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:01:27 2019

@author: abdullah
"""

def n_queens(n):
    """
        input: n - number of rows = number of columns = number of rows
        output: non-attacking placements for n queens
        
        time complexity ~ tends to O(n! / c^n), where c =  2.54, which is super-exponential
    """
    def solve_n_queens(row):
        if row == n:
            result.append(list(col_placement))
            return
        for col in range(n):
            if all(abs(c - col) not in (0, row - i) for i, c in enumerate(col_placement[:row])):
                col_placement[row] = col
                solve_n_queens(row+1)
                
    result, col_placement = [], [0] * n
    solve_n_queens(0)
    return result
