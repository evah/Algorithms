#!/usr/bin/env python
# -*- coding: utf-8 -*-

n,x=map(int,input().split())

l=[list(map(float,input().split())) for _ in range(x) ]
# l=[[89.0, 90.0, 78.0, 93.0, 80.0], [90.0, 91.0, 85.0, 88.0, 86.0], [91.0, 92.0, 83.0, 89.0, 90.5]]
# zip(*l)=[(89.0, 90.0, 91.0), (90.0, 91.0, 92.0), (78.0, 85.0, 83.0), (93.0, 88.0, 89.0), (80.0, 86.0, 90.5)]

[print(sum(i)/x) for i in zip(*l)]
