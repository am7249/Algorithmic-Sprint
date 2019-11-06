#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:22:13 2019

@author: macbook
"""

def add_pair(values, target):
    val_comp = {}
    for value in range(len(values)):
        val_comp[values[value]] = value
    for value in values:
        diff = target - value
        if diff in val_comp:
            return values.index(value), val_comp[diff]
    return False


def vertex_dist(points, vertex, k):
    points_distance = []
    for point in points:
        dist = 0
        for i in range(2):
            dist += (point[i] - vertex[i])**2
        points_distance.append(dist)
        

def dutch_flag(A,k):
    pivot = A[k]
    smaller = equal = 0
    larger = len(A)
    
    while equal < larger:
        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: #A[equal] > pivot
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]
    return A

def increment_integer(A):
    
    for i in reversed(range(len(A))):
        if A[i] < 9:
            A[i] += 1
            return A
        elif A[i] == 9:
            A[i] = 0
            if i == 0:
                return [1] + A[:]

def multiply_two_integers(A,B):
    sign = -1 if A[0] ^ B[0] else 1
    A[0], B[0] = abs(A[0]), abs(B[0])
    ans = [0] * (len(A) + len(B))
    
    for i in reversed(range(len(B))):
        for j in reversed(range(len(A))):
            res = B[i] * A[j]
            ans[i + j + 1] += res
            ans[i + j] += ans[i+j+1]//10
            ans[i + j + 1] %= 10
    start = 0
    while ans[start] == 0:
        start += 1
    ans[start] *= sign
    return ans[start:]

def advance_through_array(A):
    _max = 0
    for i in range(len(A)):
        if i + A[i] > _max:
            if i <= _max:
                _max = i + A[i]
    if _max >= len(A) - 1:
        return True
    return False

def delete_duplicates(A):
    if not A:
        return 0
    
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return A

def sell_stock_once(A):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in A:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit

def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2)
    

def enumerate_primes(n):
    ans = list(range(2,n+1))
    
    for i in range(len(ans)):
        if ans[i] > 0:
            for j in range(i+1,len(ans)):
                if ans[j] % ans[i] == 0:
                    ans[j] = 0
        else:
            pass
    return ans

def permutation(A, perm):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    for i in range(len(A)):
        next = i
        #resolve each cycle within the while loop
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i] #swap the current element with the target element
            temp = perm[next] #store the current permutation index
            perm[next] -= len(perm) #mark it so that you know when the cycle ends
            next = temp #now go to the permutation index you stored. Essentially you are resolving the cycle in order
    perm[:] = [a + len(perm) for a in perm] #restore the permutation list
    return A



#print(permutation(['a','b','c','d'],[0,2,3,1]))
#print(enumerate_primes(18))
#print(sell_stock_once([310,315,275,295,260,270,290,230,255,250]))
#print(delete_duplicates([2,3,5,5,7,11,11,11,13]))
#print(advance_through_array([0,2,2,2,2,0,1]))
#print(multiply_two_integers([1,9,3,7,0,7,7,2,1],[-7,6,1,8,3,8,2,5,7,2,8,7]))
#print(increment_integer([9,9,9]))
#print(dutch_flag([0,1,9,3,2,5,1,7,7,2,6,1,2,3,5,5], 5))
#print(vertex_dist([[0,0],[1,9],[2,4],[4,1],[2,2],[2,1]],[2,2],2))
#print(add_pair([14, 13, 6, 7, 8, 10, 1, 2], 3))