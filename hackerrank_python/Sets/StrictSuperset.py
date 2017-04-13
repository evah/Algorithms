#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = set(input().split())
test_num = int(input())
print(all(a > set(input().split()) for _ in range(test_num)))
