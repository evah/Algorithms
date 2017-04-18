#!/usr/bin/env python
# -*- coding: utf-8 -*-
N,n = int(input()),input().split()
print (all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n]))
