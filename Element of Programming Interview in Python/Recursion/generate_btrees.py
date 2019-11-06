#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 20:18:28 2019

@author: abdullah
"""

class BinaryTreeNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def generate_binary_trees(num_nodes):
    """
        input: number of nodes in a binary tree
        output: all possible binary trees with the input number of nodes
    """
    
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