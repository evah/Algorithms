#!/usr/bin/env python
# -*- coding: utf-8 -*-
_ , M = input(), set(map(int,input().split()))
_ , N = input(), set(map(int,input().split()))
print(*sorted(list(M.symmetric_difference(N))),sep='\n')
# it is the same: print(*sorted(list(M^N)),sep='\n')
# it is equivalent to print("\n".join($THE_LIST))
