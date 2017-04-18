#!/usr/bin/env python
# -*- coding: utf-8 -*-
def merge_the_tools(string, k):
    S, N = string, k 
    
    for part in zip(*[iter(S)] * N):
        # zip(*[iter(S)] * N) = [('A', 'A', 'B'), ('C', 'A', 'A'), ('A', 'D', 'A')]
        d = dict()
        # ''.join only applies to the keys
        print(''.join([d.setdefault(c, c) for c in part if c not in d ]))
        
