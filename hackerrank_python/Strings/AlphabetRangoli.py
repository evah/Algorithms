#!/usr/bin/env python
# -*- coding: utf-8 -*-
def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase

    n = size
    L = []
    for i in range(n):
        #http://stackoverflow.com/questions/21617586/reverse-string-string-1-works-but-string0-1-and-others-dont
        s = "-".join(alpha[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-")) 
        #if n = 5, the number of elements in a row would be 17
    print('\n'.join(L[:0:-1]+L))
