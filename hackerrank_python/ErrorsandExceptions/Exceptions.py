#!/usr/bin/env python
# -*- coding: utf-8 -*-
for i in range(int(input())):
    a, b = input().split()
    try:
        div = int(a) // int(b)
        print(div)
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code: {}".format(e))
