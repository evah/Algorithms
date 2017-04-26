#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but it has one difference: The value fields' data type is specified upon initialization.
'''
from collections import defaultdict

n, m = map(int, input().split())

d = defaultdict(list)
[d[input()].append(str(i + 1)) for i in range(n)]
[print(' '.join(d[input()]) or -1) for _ in range(m)]
