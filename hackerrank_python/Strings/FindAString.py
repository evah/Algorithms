#!/usr/bin/env python
# -*- coding: utf-8 -*-
def count_substring(string, sub_string):
    m = len(string)-len(sub_string)
    n = len(sub_string)
    count = 0
    
    for i in range(0,m+1): 
        if sub_string == string[i:i+n]: 
            count = count+1
            
    return count
