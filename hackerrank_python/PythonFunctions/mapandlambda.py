#!/usr/bin/env python
# -*- coding: utf-8 -*-
cube = lambda x: x**3 # complete the lambda function 

l = [0,1]
def fibonacci(n):
    # return a list of fibonacci numbers
    for _ in range(n-2):
        l.append(l[-1]+l[-2])
    return l[:n]

list(map(cube,l))
