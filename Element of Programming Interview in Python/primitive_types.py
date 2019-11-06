#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:26:38 2019

@author: macbook
"""
#import sys


def count_bits(n):
    num_bits = 0
    while n:
        num_bits += 1
        n &= n - 1
    return num_bits

def parity_1(x):
    """ time complexity = O(n) where n = word size"""
    bits = count_bits(x)
    if bits % 2 == 1:
        return 1
    elif bits % 2 == 0:
        return 0
    else:
        raise Exception
        
def parity_2(x):
    """time complexity = O(k) where k = no. of bits set to 1"""
    
    result = 0
    while x:
        result ^= 1
        x &= x - 1 #drops the lowest set bit of x
    return result

def parity_3(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x >> MASK_SIZE & BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK])
    
def parity_4(x, word):
    while word > 1:
        x = x ^ (x >> int(word/2))
        word /= 2
    
    return x & 0x1
    
    
def swap_bit(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = (1 << i) | (1 << j)
        x = x ^ bit_mask
        return x




#print(count_bits(140))
#print(parity_4(140,64))
print(swap_bit(8, 0, 3))