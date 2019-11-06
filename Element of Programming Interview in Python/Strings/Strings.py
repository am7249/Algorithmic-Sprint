#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:31:14 2019

@author: macbook
"""

import random
import math
import bisect
import itertools
import functools


def is_palindrome(s):
    start, end = 0, len(s) - 1
    while start < end:
        if s[start] == s[end]:
            start, end = start + 1, end - 1
        else:
            return False
    return True

def is_palindrome_short(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))


def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
        
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break
    
    return ('-' if is_negative else '') + ''.join(reversed(s))

def str_to_int(s):
    return functools.reduce(
            lambda running_sum, c: running_sum * 10 + s.index(c),
            s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


def string_to_integer(s):
    s = s.strip()
    l = []
    for i in s:
        digit = ord(i) - 48
        l.append(digit)
    num = 0
    l.reverse()
    for j in range(len(l)):
        num += l[j] * (10 ** j)
    return num

def ss_decode_col_id(col):
    return functools.reduce(
            lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)
    
def replace_and_remove(size, s):
    write_idx, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] = s[i]
            write_idx += 1
        if s[i] == 'a':
            a_count += 1
    
    curr_idx = write_idx - 1
    write_idx += a_count - 1
    final_size = write_idx + 1
    
    while curr_idx >= 0:
        if s[curr_idx] == 'a':
            s[write_idx - 1 : write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            s[write_idx] = s[curr_idx]
            write_idx -= 1
        curr_idx -= 1
    return final_size


def palindromity_spacy(string):
    char = []
    for i in string:
        if 97 <= ord(i) <= 122:
            char.append(i)
        elif 65 <= ord(i) <= 90:
            char.append(chr(ord(i) + 32))
        else:
            pass
    
    start, end = 0, len(char) - 1
    while start < end:
        if char[start] == char[end]:
            start, end = start + 1, end - 1
        else:
            return False
    
    return True

def palindromity_good(string):
    i, j = 0, len(string) - 1
    while i < j:
        while not string[i].isalnum() and i < j:
            i += 1
        while not string[j].isalnum() and i < j:
            j -= 1
        if string[i].lower() != string[j].lower():
            return False
        i, j = i + 1, j - 1
    return True

def reverse_sentence_naive(sent):
    words = sent.split(" ")
    start, end = 0, len(words) - 1
    if len(sent) <= 1:
        return sent
    
    while start < end:
        words[start], words[end] = words[end], words[start]
        start, end = start + 1, end - 1
    
    return " ".join(words)

def reverse_sentence_better(sent):
    
    sent.reverse() #sent is a bytearray
    
    def reverse_word(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
            
    start = 0
    while True:
        end = sent.find(b' ', start)
        if end < 0:
            break
        reverse_word(sent, start, end - 1)
        start = end + 1
    reverse_word(sent, start, len(sent) - 1)
    return sent
    
def look_and_say(n):
    
    def next_number(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                i += 1
                count += 1
            result.append(str(count) + s[i])
            i += 1
        return "".join(result)
    
    s = "1"
    for _ in range(n):
        s = next_number(s)
    return s
    
def roman_to_decimal(string):
    value = 0
    for digit in range(len(string) - 1):
        if string[digit] == "I":
            next_dig = string[digit + 1]
            if next_dig == "V":
                value += 49
            elif next_dig == "X":
                value += 9
            else:
                value += 1
        elif string[digit] == "V":
            value += 5
        elif string[digit] == "X":
            next_dig = string[digit + 1]
            if next_dig == "L":
                value += 40
            elif next_dig == "C":
                value += 90
            else:
                value += 10
        elif string[digit] == "L":
            value += 50
        elif string[digit] == "C":
            next_dig = string[digit + 1]
            if next_dig == "D":
                value += 400
            elif next_dig == "M":
                value += 900
            else:
                value += 100
        elif string[digit] == "D":
            value += 500
        elif string[digit] == "M":
            value += 1000
        else:
            raise Exception("Invalid Roman Number")
    return value

def roman_to_decimal_dict(s):
    vals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    
    value = 0
    for i in reversed(range(len(s)-1)):
        if vals[s[i]] < vals[s[i+1]]:
            value -= vals[s[i]]
        else:
            value += vals[s[i]]
    value += vals[s[-1]]
    return value

def valid_ip(s):
    def is_valid(s):
        return len(s) == 1 or (s[0] != 0 and int(s) <= 255)
    
    result, parts = [], [None] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid(parts[0]):
            for j in range(1, min(4, len(s) - i)):
                parts[1] = s[i:i + j]
                if is_valid(parts[1]):
                    for k in range(1, min(4, len(s) - i - j)):
                        parts[2], parts[3] = s[i+j:i+j+k], s[i+j+k:]
                        if is_valid(parts[2]) and is_valid(parts[3]):
                            result.append(".".join(parts))
    return result

def sinusoidally(s):
    result = []
    for i in range(1,len(s),4):
        result.append(s[i])
    for j in range(0,len(s),2):
        result.append(s[j])
    for k in range(3,len(s),4):
        result.append(s[k])
    
    return "".join(result)

def sinusoidally_pythonic(s):
    return s[1::4] + s[0::2] + s[3::4]

def rle_encoding(s):
    result = []
    i, j = 0, 0
    while i < len(s):
        count = 0
        while j < len(s) and s[j] == s[i]:
            j, count = j + 1, count + 1
        result.append(str(count) + s[i])
        i = j
    return "".join(result)

def rle_decode(s):
    result = []
    for i in range(0,len(s),2):
        letter = s[i+1]
        for i in range(int(s[i])):
            result.append(letter)
    return "".join(result)
"""========================================================================="""
#base conversion

def frm(x, b):
    """
    Converts given number x, from base 10 to base b 
    x -- the number in base 10
    b -- base to convert
    """
    assert(x >= 0)
    assert(1< b < 37)
    r = ''
    import string
    while x > 0:
        r = string.printable[x % b] + r
        x //= b
    return r
def to(s, b):
    """
    Converts given number s, from base b to base 10
    s -- string representation of number
    b -- base of given number
    """
    assert(1 < b < 37)
    return int(s, b)
def convert(s, a, b):
    """
    Converts s from base a to base b
    """
    return frm(to(s, a), b)

#print(convert("615",7,13))


"""========================================================================="""
print(rle_decode("4a1b3c2a"))
#print(rle_encoding("aaaabbbcccaa"))
#print(sinusoidally_pythonic("Hello_World!"))
#print(valid_ip("19216811"))
#print(roman_to_decimal_dict("LVIIII"))
#print(look_and_say(10))
#print(reverse_sentence_better(my_string))
#print(palindromity_good("A man, a plan, a canal, Panama"))
#print(replace_and_remove(4,['a','c','a','a','_','_','_']))
#print(ss_decode_col_id('DD'))
#print(base_conversion('615',7,13))
#print(gstring_to_integer('435'))