#!/usr/bin/env python
# -*- coding: utf-8 -*-
def swap_case(s):
    s_swap=''.join([i.lower() if i.isupper() else i.upper() for i in s])
    return s_swap
