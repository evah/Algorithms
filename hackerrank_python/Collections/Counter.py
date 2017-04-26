#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

shoes_num, sizes, inputs = int(input()),  map(int,input().split()),  int(input())

sizes = Counter(sizes)
total = 0

for _ in range(inputs):
    size, price = map(int, input().split())   
    if size in sizes and sizes[size]>0:
           sizes[size] -= 1
           total += price

print(total)
