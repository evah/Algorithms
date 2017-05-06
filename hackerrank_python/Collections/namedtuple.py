#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple

anz=int(input()); student = namedtuple('student', input().split())
arr = [student(*input().split()) for _ in range(anz)]
print(float(sum(int(student.MARKS) for student in arr))/len(arr))
