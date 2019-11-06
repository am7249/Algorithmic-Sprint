#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 13:22:16 2019

@author: macbook
"""

"""RECURSION IN DEPTH"""


class BinaryTreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

import os

def empty_vase(n):
    if n == 0:
        return 0
    else:
        return 1 + empty_vase(n-1)
    

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

NUM_PEGS = 5

def tower_of_hanoi(num_rings):
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
    
    return result, pegs


def n_queens(n):
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

def permutations(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            directed_permutations(i+1)
            A[i], A[j] = A[j], A[i]
    result = []
    directed_permutations(0)
    return result
    

def generate_power_set(input_set):
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


def combinations(n,k):
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(list(partial_combination))
            return
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i+1, partial_combination + [i])
            i += 1
            
    result = []
    directed_combinations(1,[])
    return result

def generate_balanced_parenthesis(num_pairs):
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


def palindromic_decompositions(input_string):
    def directed_palindromic_decomposition(offset, decomp):
        if offset == len(input_string):
            result.append(list(decomp))
            return 
        for i in range(offset+1,len(input_string)+1):
            prefix = input_string[offset:i]
            if prefix == prefix[::-1]:
                directed_palindromic_decomposition(i, decomp+[prefix])
    result = []
    directed_palindromic_decomposition(0,[])
    return result

def generate_binary_trees(num_nodes):
    if num_nodes == 0:
        return [None]
    result = []
    for num_left_subtree_nodes in range(num_nodes):
        num_right_subtree_nodes = num_nodes - 1 - num_left_subtree_nodes
        left_subtree = generate_binary_trees(num_left_subtree_nodes)
        right_subtree = generate_binary_trees(num_right_subtree_nodes)
        
        result += [
                BinaryTreeNode(0,left,right)
                for left in left_subtree
                for right in right_subtree]
    return result
        

"""========================================================================="""

"""
Four recursive problems implemented in Python
    - Factorial Function
    - English Ruler
    - Binary Search
    - File System
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)
    
def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(major_length, num_inches):
    draw_line(major_length, '0')
    for j in range(1, num_inches+1):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
        
def search(data, target):
    low, high = 0, len(data) - 1
    def binary_search(data, target, low=low, high=high):
        if low > high:
            return False
        else:
            mid = (low + high) // 2
            if target == data[mid]:
                return mid
            elif target < data[mid]:
                return binary_search(data, target, low, mid - 1)
            else:
                return binary_search(data, target, mid + 1, high)
    return binary_search(data, target, low, high)

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    print('{0:<7}'.format(total),path)
    return total



#print(disk_usage('/Users'))
#print(search([1,2,3,4,5,6,7,8,9,10],8))
#print(draw_ruler(4,1))    
#print(factorial(5))
"""========================================================================="""

print(generate_binary_trees(3))
#print(palindromic_decompositions("0204451881"))
#print(generate_balanced_parenthesis(4))
#print(combinations(4,2))
#print(generate_power_set([1,2]))
#print(permutations([2,3,5,7,1]))
#print(n_queens(8))
#print(tower_of_hanoi(NUM_PEGS)[1])


#print(find_max([1,4,2,4,6,7,2,3,43,2]))
