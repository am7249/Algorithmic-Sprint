#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 16:51:39 2019

@author: macbook
"""

class Node:
    
    __slots__ = '_element','_left','_right'    
    
    def __init__(self, element=0, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right
        


class Stack_Array: 
    """Implementation of Stack API using python list."""
    
    def __init__(self):
        self.data = []
        self.max = [float('-inf')]
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get_max(self):
        return self.max[-1]
    
    def push(self, elem):
        self.data.append(elem)
        self.size += 1
        if elem > self.max[-1]:
            self.max.append(elem)
        
    def pop(self):
        if not self.is_empty():
            value = self.data.pop()
            self.size -= 1
            if value == self.get_max():
                self.max.pop()
        return value

class Stack_List:
    
    class Node:
        __slots__ = "data","next"
        
        def __init__(self,data=0,next=None):
            self.data = data
            self.next = next
    
    
    def __init__(self):
        self.head = self.Node(None,None)
        self.tail = self.Node(None,None)
        self.head.next = self.tail
        self.curr = None
        self.curr_prev = self.Node(None,None)
        self.size = 0
        self.max = [float('-inf')]
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get_max(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        return self.max[-1]
    
    def push(self, elem):
        if self.is_empty():
            self.head.next = self.Node(elem,self.tail)
            self.curr = self.head.next
            self.curr_prev.next = self.curr
            self.size += 1

        else:
            self.curr.next = self.Node(elem,self.tail)
            self.curr_prev = self.curr
            self.curr = self.curr.next
            self.curr.next = self.tail
            self.size += 1
            
        if elem > self.max[-1]:
                self.max.append(elem)
    
    def pop(self):
        if self.is_empty():
            raise Exception('Empty Stack')
        value = self.curr.data
        self.curr.data = None
        self.curr.next = None
        self.tail = self.curr
        self.curr = self.curr_prev
        self.size -= 1
        
        if value == self.get_max():
            self.max.pop()
        return value


def RPN_expression(expression):
    intermediate_results = []
    DELIMETER = ','
    OPERATORS = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: y * x,
            '/': lambda y, x: int(x / y)}
    
    for token in expression.split(DELIMETER):
        if token in OPERATORS:
            intermediate_results.append(OPERATORS[token] (intermediate_results.pop(), intermediate_results.pop()))
        else:
            intermediate_results.append(int(token))
        
    return intermediate_results[-1]
        
    
def well_formedness(string):
    stack, OPERATORS = [], {
                    ')':'(',
                    ']':'[',
                    '}':'{'}
    for i in string:
        if i in list(OPERATORS.values()):
            stack.append(i)
        elif i in list(OPERATORS.keys()):
            if stack:
                v = stack[-1]
                if v == OPERATORS[i]:
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
    return len(stack) == 0

def buildings_sunset(buildings):
    stack = []
    for building in buildings:
        print(stack,'\n')
        if not stack:
            stack.append(buildings[building])
        else:
            while buildings[building] >= stack[-1]:
                stack.pop()
                if len(stack) == 0:
                    break
            stack.append(buildings[building])
    return stack

import collections

def binary_tree_depth(binary_tree):
    nodes_q = []
    if not binary_tree:
        return nodes_q
    
    curr_depth_nodes = [binary_tree]
    while curr_depth_nodes:
        nodes_q.append([curr._element for curr in curr_depth_nodes])
        curr_depth_nodes = [
                child
                for curr in curr_depth_nodes 
                for child in (curr._left, curr._right)
                if child
            ]
    return nodes_q

class ArrayQueue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._first = 0
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first_elem(self):
        if self.is_empty():
            raise Exception('Empty Queue')
        return self._data[self._first]
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Empty Queue')
        value = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % len(self._data)
        self._size -= 1
        
        return value
    
    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._first + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
        
    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._first
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._first = 0
                
        
class QueueStack:
    
    def __init__(self):
        self.enq, self.deq = [], []
        
    def enqueue(self, e):
        self.enq.append(e)
        
    def dequeue(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        
        if not self.deq:
            raise Exception('Empty Stack')
            
        return self.deq.pop()

if __name__ == "__main__":
    #myStack = Stack_List()
    
    #for i in range(0,150,23):
    #    myStack.push(i)
    
    #for i in range(150,0,-25):
    #    myStack.push(i)
    
    #for _ in range(7):
    #    value = myStack.pop()
    #    print(value)
    
    #B = Node(314)
    #B._left, B._right = Node(6), Node(6)
    #B._left._left, B._left._right, B._right._left, B._right._right = (Node(271),
    #                                                                  Node(561),
    #                                                                  Node(2),
    #                                                                  Node(271))
    
    Q = ArrayQueue()
    
    for i in range(9):
        Q.enqueue(i)
    for i in range(9):
        Q.enqueue(i)
    v = Q.dequeue()
    print(Q.DEFAULT_CAPACITY)
    
    #print(binary_tree_depth(B))
    
    #print(buildings_sunset({'a':2, 'b':3, 'c':4, 'd':12, 'e':2, 'f':4, 'g':3,
    #                        'h':10, 'i':9, 'j':4, 'k':5, 'l':6}))
    #print(well_formedness(""))
    #print(RPN_expression("2,1,+,3,*"))