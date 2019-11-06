#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:13:09 2019

@author: abdullah
"""

def generate_balanced_parenthesis(num_pairs):
    """
        input: number of matched pairs of parenthesis
        output: matched parenthesis
        
        time complexity ~ O((2k)! / k!(k+1)!)
    """
    def directed_balanced_parenthesis(num_left_parens_needed,
                                      num_right_parens_needed,
                                      valid_prefix,
                                      result=[]):
        if num_left_parens_needed > 0:
            directed_balanced_parenthesis(num_left_parens_needed - 1,
                                          num_right_parens_needed,
                                          valid_prefix + '(')
            
        if num_left_parens_needed < num_right_parens_needed:
            directed_balanced_parenthesis(num_left_parens_needed,
                                          num_right_parens_needed - 1,
                                          valid_prefix + ')')
        if num_right_parens_needed == 0:
            result.append(valid_prefix)
        return result
    
    return directed_balanced_parenthesis(num_pairs, num_pairs, '')