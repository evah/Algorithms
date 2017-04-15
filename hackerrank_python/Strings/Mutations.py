#!/usr/bin/env python
# -*- coding: utf-8 -*-
def mutate_string(string, position, character):
    a = list(string)
    a[position]=character
    string2 = ''.join(a)
    return string2
