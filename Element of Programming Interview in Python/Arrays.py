#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:37:01 2019

@author: macbook
"""
import random
import bisect
import itertools

def even_odd(A):
    """take advantage of the fact that you can operate on both ends
    effectively. Partition the array into Even, Unclassified, and Odd.
    Initially Even and Odd are empty, we iterate through the Unclassified
    and keep filling Even and Odd. 
    O(n) time complexity and O(1) space complexity"""
    
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A


def dutch_flag_1(A, i):
    """
    time complexity = O(n)
    space complexity = O(n)    
    """
    _A = []
    pivot = A[i]
    for elem in A:
        if elem < pivot:
            _A.append(elem)
    for elem in A:
        if elem == pivot:
            _A.append(elem)
    for elem in A:
        if elem > pivot:
            _A.append(elem)
    
    return _A

def dutch_flag_2(A, i):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    l, p1, g = 0, 0, len(A) - 1
    pivot = A[i]
    
    while p1 < g:
        if A[p1] < pivot:
            A[l], A[p1] = A[p1], A[l]
            l, p1 = l + 1, p1 + 1
        elif A[p1] == pivot:
            p1 += 1
        else:
            g -= 1
            A[p1], A[g] = A[g], A[p1]
    return A

def increment(A):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    
    #carry = False
    for i in range(len(A)-1,-1,-1):
        if A[i] + 1 <= 9:
            A[i] += 1
            break
        elif A[i] + 1 > 9:
            if i == 0:
                A[i] = 1
                A.append(0)
            else:
                A[i] = 0
    return A

def multiply(A, B):
    """
    time complexity = O(nm)
    space complexity = O(n + m)
    """
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    A[0], B[0] = abs(A[0]), abs(B[0])
    
    result = [0] * (len(A) + len(B))
    
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            result[i + j + 1] += A[i] * B[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    result = result[next((i for i, x in enumerate(result)
                        if x != 0), len(result)):] or [0]
    
    return [sign * result[0]] + result[1:]

def can_reach_end(A):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    furthest, end_index = 0, len(A)-1
    i = 0
    min_steps = 0
    
    while i <= furthest and furthest < end_index:
        new_furthest = max(furthest, A[i] + i)
        if new_furthest != furthest:
            min_steps += 1
        furthest = new_furthest
        i += 1
    if furthest >= end_index:
        return True, min_steps
    else:
        return False
    
def remove_duplicates(A):
    i, j = 0, 0
    while j < len(A) - 1:
        if A[j+1] != A[j]:
            i = i + 1
            j = j + 1
            A[i] = A[j]

        elif A[j+1] == A[j]:
            j = j + 1
            
    return i + 1

def remove_duplicates_2(A):
    if not A:
        return 0
    
    write_index = 1
    for i in range(1,len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index

def buy_sell_stocks(A):    
    max_profit = float('-inf')
    buy, sell = 0,0
    
    while sell < len(A):
        if A[sell] <= A[buy]:
            buy = sell
            sell += 1
        elif A[sell] > A[buy]:
            if A[sell] - A[buy] > max_profit:
                max_profit = A[sell] - A[buy]
                sell += 1
            
    return max_profit


def buy_sell_stocks_2(A):
    min_price_so_far, max_profit = float('inf'), 0.0
    for price in A:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    return max_profit
        

def alternation_bad(A):
    alter = [0] * len(A)
    
    for i in range(1,len(A),2):
        elem = max(A)
        alter[i] = elem
        A[A.index(elem)] = 0
    
    for i in range(0,len(A),2):
        elem = max(A)
        alter[i] = elem
        A[A.index(elem)] = 0
        
    return alter

def alternation(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2)
    return A

def primes(n):
    count = [False, False] + [True]*(n-1)
    prime = []
    
    for p in range(2, n+1):
        if count[p]:
            prime.append(p)
            for i in range(p, n+1, p):
                count[i] = False
    return prime
                
def permutations(A,P):
    """
    time complexity = O(n)
    space complexity = O(n)
    """
    perm = [0] * len(A)
    for i in range(len(A)):
        perm[P[i]] = A[i]
    return perm

def permutation_2(A, perm):
    """
    time complexity = O(n)
    space complexity = O(1)
    """
    for i in range(len(A)):
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            perm[next] -= len(perm)
            next = temp
    perm[:] = [a + len(perm) for a in perm]
    
def next_permutation(P):
    inversion_point = len(P) - 2
    while (inversion_point >= 0 and P[inversion_point] >= P[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []
    
    for i in reversed(range(inversion_point + 1, len(P))):
        if P[i] > P[inversion_point]:
            P[inversion_point], P[i] = P[i], P[inversion_point]
            break
    
    P[inversion_point + 1:] = reversed(P[inversion_point + 1:])
    return P



def prev_permutation(P):
    inversion_point = len(P) - 2
    while (inversion_point >= 0 and P[inversion_point] <= P[inversion_point+1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []
    
    for i in reversed(range(inversion_point + 1, len(P))):
        if P[i] < P[inversion_point]:
            P[inversion_point], P[i] = P[i], P[inversion_point]
            break
    P[inversion_point + 1:] = reversed(P[inversion_point + 1:])
    return P
    

def sample_data(A, size):
    if len(A) != len(set(A)):
        raise Exception("Duplicates present in the list")
    for i in range(size):
        r = random.randint(i,len(A)-1)
        A[i], A[r] = A[r], A[i]
    return A[:size]

def random_permutation(n):
    perm = list(range(n))
    sample_data(perm,n)
    return perm

def random_subset(n, k):
    change_ind = {}
    for i in range(k):
        rand_idx = random.randrange(i,n)
        rand_idx_mapped = change_ind.get(rand_idx,rand_idx)
        i_mapped = change_ind.get(i, i)
        change_ind[rand_idx] =  i_mapped
        change_ind[i] = rand_idx_mapped
    return [change_ind[i] for i in range(k)]

def non_uniform_sampling(values, probabilities):
    partitions = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(partitions, random.random())
    return values[interval_idx]

def duplicates(nums):
    
    #solution with hashtable
    result = []
    for i in nums:
        index = abs(i) - 1
        if nums[index] >= 1:
            nums[index] *= -1
        elif nums[index] < 0:
            result.append(i)
        else:
            raise Exception('0 is in the list')
    return result


"""========================================================================="""
def dutch_flag_test(A, idx):
    pivot = A[idx]
    smaller, equal, larger = 0, 0, len(A)
    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal = equal + 1
        else:
            larger = larger - 1
            A[equal], A[larger] = A[larger], A[equal]
    return A
    
    
    
def increment_test(A):
    for digit in reversed(range(len(A))):
        if A[digit] + 1 <= 9:
            A[digit] += 1
            break
        else:
            if digit == 0:
                A[digit] = 1
                A.append(0)
            else:
                A[digit] = 0
    return A


def multiply_test(A,B):
    sign = -1 if (A[0] < 0 ^ B[0] < 0) else 1
    array = [0] * (len(A) + len(B))
    
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            array[i + j + 1] += A[i] * B[j]
            array[i + j] += array[i + j + 1] // 10
            array[i + j + 1] %= 10
    
    for idx in range(len(array)):
        if array[idx] != 0:
            break
    
    if sign == -1:
        array[idx] *= sign
    return array[idx:]


def sum_pair(A, x):
    if len(A) < 2:
        raise Exception('Not enough numbers in the array')
    mem = {}
    for i in range(len(A)):
        diff = x - A[i]
        if diff in mem:
            return True
        else:
            mem[diff] = i
    return False







"""========================================================================="""


print(duplicates([2,1,2,1,3,4,5]))
#print(sum_pair([1,4,2,3,9,4],8))
#print(multiply_test([1,2,4],[2,3]))
#print(dutch_flag_test([3,2,5,6,7,3,2,6,7,9,2,4,8,12,5,5,5],2))
#print(increment_test([9,9,9]))
#print(non_uniform_sampling([3,5,7,11],[9/18,6/18,2/18,1/18]))
#print(random_subset(4,2))
#print(random_permutation(27))    
#print(sample_data([1,2,3,4,5,6],4))
#print(next_permutation([1,0,3,2]))
#print(prev_permutation([3,1,0,2,4,6]))
#print(permutation_2(['a','b','c','d'],[2,0,1,3]))
#print(primes(18))        
#print(alternation([1,2,3,4,5,6,7,8,9]))
#print(buy_sell_stocks_2([310,315,298,270,300,330,210]))
#print(buy_sell_stocks([310,315,298,378]))
#print(remove_duplicates([2,3,5,5,7,11,11,11,13]))
#print(can_reach_end([3,3,1,0,2,0,1,0]))
#print(multiply([-1,3,4],[1,3,2]))
#print(increment([9,9,9]))        
#print(even_odd([3,2,5,6,7,3,2,6,7,9,2,4,8,12]))
#print(dutch_flag_2([3,2,5,6,7,3,2,6,7,9,2,4,8,12], 2))
