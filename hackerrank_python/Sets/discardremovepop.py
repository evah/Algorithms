#!/usr/bin/env python
# -*- coding: utf-8 -*-
n = int(input())
s = set(map(int, input().split())) 

m = int(input())
for i in range(m):
        eval('s.{0}({1})'.format(*input().split()+['']))

        print(sum(s))
