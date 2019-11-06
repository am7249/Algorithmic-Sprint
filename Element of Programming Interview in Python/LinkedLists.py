#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:56:41 2019

@author: macbook
"""

class Node:
    
    __slots__ = '_element','_next'    
    
    def __init__(self, element=0, next=None):
        self._element = element
        self._next = next
        
        
def merge_two_sorted_lists(L1, L2):
    if L1._element < L2._element:
        dummy_head = L1
        start = L1
        compare = L2
    else:
        dummy_head = L2
        start = L2
        compare = L1
    
    while start._next != None:
        if start._next._element <= compare._element:
            start = start._next
        else:
            temp = compare._next
            compare._next = start._next
            start._next = compare
            compare = temp
    if compare != None:
        start._next = compare
    return dummy_head
        
def merge_two_sorted_book(L1, L2):
    dummy_head = tail = Node()
    
    while L1 and L2:
        if L1._element < L2._element:
            tail._next, L1 = L1, L1._next
        else:
            tail._next, L2 = L2, L2._next
        tail = tail._next 
    
    tail._next = L1 or L2
    return dummy_head._next

def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = Node(0,L)
    for _ in range(1,start):
        sublist_head = sublist_head._next
    
    sublist_iter = sublist_head._next
    
    for _ in range(finish - start):
        temp = sublist_iter._next
        sublist_iter._next, temp._next, sublist_head._next = (temp._next,
                                                              sublist_head._next,
                                                              temp)
    return dummy_head._next

def cyclicity_spacy(L):
    mark = [L]
    while L._next != None:
        if L._next not in mark:
            mark.append(L._next)
            L = L._next
        else:
            return L
    return None

def cyclicity(L):
    i, j = L, L
    while j and j._next and j._next._next:
        j = j._next._next
        i = i._next
        
        if i == j:
            return i._next
    return None

def overlap(L1, L2):
    dummy_L1, dummy_L2 = Node(0,L1), Node(0,L2)
    while dummy_L1._next != None:
        dummy_L1 = dummy_L1._next
    while dummy_L2._next != None:
        dummy_L2 = dummy_L2._next
    
    if dummy_L1 == dummy_L2:
        return True
    return False

def overlap_position(L1, L2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L._next
        return length
    
    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1
    
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2._next
    
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1._next, L2._next
    return L1


def delete_node(node):
    node._element = node._next._element
    node._next = node._next._next
    
def delete_kth_last_node(L,k):
    dummy_head = start = end = L
    
    for _ in range(k+1):
        end = end._next
    
    while end._next != None:
        start, end = start._next, end._next
    
    start._next = start._next._next
    
    return start

def delete_duplicates_list(L):
    dummy_head = Node(0,L)
    i = j = L
    
    while j:
        while (j._next != None) and (j._next._element == j._element):
            j = j._next
        i._next = j._next
        i = j = j._next
    
    return dummy_head._next

def cyclic_shift(L, k):
    dummy_head = Node(0, L)
    i = j = L
    
    for _ in range(k):
        j = j._next
    
    while j._next != None:
        i, j = i._next, j._next
    
    dummy_head._next = i._next
    i._next = None
    j._next = L
    
    return dummy_head._next

def even_odd_merge(L):
    dummy_head = Node(0,L)
    start, odd_first = L, L._next
    
    while start._next != None:
        temp = start._next
        start._next = start._next._next
        start = temp
    start._next = odd_first
    
    return dummy_head._next

def test_palindromity(L):
    slow = fast = L
    count = 0
    while fast and fast._next:
        count += 1
        fast, slow = fast._next._next, slow._next

    first_half_iter, second_half_iter = L, reverse_sublist(slow, count-1, 2*count-1)
    while second_half_iter and first_half_iter:
        if second_half_iter._element != first_half_iter._element:
            return False
        second_half_iter, first_half_iter = second_half_iter._next, first_half_iter._next
    
    return True

def list_pivoting(L,k):
    
    smaller_head = smaller_iter = Node()
    equal_head = equal_iter = Node()
    larger_head = larger_iter = Node()
    
    while L:
        if L._element < k:
            smaller_iter._next = L
            smaller_iter = smaller_iter._next
        elif L._element == k:
            equal_iter._next = L
            equal_iter = equal_iter._next
        else:
            larger_iter._next = L
            larger_iter = larger_iter._next
        L = L._next
        
    smaller_iter._next = equal_head._next
    equal_iter._next = larger_head._next
    larger_iter._next = None
    
    return smaller_head._next

def list_sum(L1, L2):
    digit_1, digit_2 = L1, L2
    a = b = power_1 = power_2 = length_1 = length_2 = 0
    
    while digit_1 or digit_2:
        if digit_1:
            a += (digit_1._element * (10 ** power_1))
            power_1 += 1
            digit_1 = digit_1._next
            length_1 += 1
        if digit_2:
            b += (digit_2._element * (10 ** power_2))
            power_2 += 1
            digit_2 = digit_2._next
            length_2 += 1
    
    result = a + b
    dummy_head = ans = Node()
    while result:
        ans._next = Node(result % 10)
        result //= 10
        ans = ans._next
    
    return dummy_head._next
    
    
    
    
    
"""========================================================================="""

L1 = Node(3)
L1._next = Node(1)
L1._next._next = Node(4)

L2 = Node(7)
L2._next = Node(0)
L2._next._next = Node(9)



"""
L2 = Node(3)
L2._next = Node(11)"""

print(list_sum(L1, L2)._next._next._next._next)

#print(list_pivoting(L1,7)._next._next._next._next._next._next._element)
#print(test_palindromity(L2))
#print(even_odd_merge(L1)._next._next._next._next._element)
#print(cyclic_shift(L2, 3)._next._next._next._next._next)
#print(delete_kth_last_node(L1,1)._next._element)

#print(overlap_position(L1,L2)._element)
#print(cyclicity(L1)._element)
#print(reverse_sublist(L1,2,4)._next._next._next._next._element)
#print(merge_two_sorted_lists(L1,L2)._next._next._next._next._next._element)