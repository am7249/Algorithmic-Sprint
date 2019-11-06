#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:23:17 2019

@author: abdullah
"""

NUM_PEGS = 3

def tower_of_hanoi(num_rings):
    """
        input: num of rings to move
        output: sequence of steps taken to move the rings
        
        time complexity ~ O(2^n)
    """
    def compute_hanoi(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_hanoi(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_hanoi(num_rings_to_move - 1, use_peg, to_peg, from_peg)
    
    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]
    compute_hanoi(num_rings, 0, 1, 2)
    
    return result

