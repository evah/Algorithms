#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

for i in range(int(input())):   
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)
