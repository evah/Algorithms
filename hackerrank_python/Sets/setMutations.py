#!/usr/bin/env python
# -*- coding: utf-8 -*-
iinput()
s1 = set(input().split())
group_num = int(input())
for i in range(group_num):
    eval('s1.{0}({1})'.format(input().split()[0], input().split()))
print(sum(map(int, s1)))
