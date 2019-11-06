#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:06:57 2019

@author: abdullah 
"""


def generate_power_set(input_set):
    """
        input: a set
        output: power set of the input set (all subsets of the input set)
        
        time complexity ~ O(n x 2^n)
        space complexity ~ O(n x 2^n)
    """
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(list(selected_so_far))
            # print(selected_so_far)
            return
        directed_power_set(to_be_selected + 1, selected_so_far)
        directed_power_set(to_be_selected + 1, selected_so_far + [input_set[to_be_selected]])
    
    power_set = []
    directed_power_set(0,[])
    return power_set
