#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = Fraction(reduce(lambda x, y : x*y, fracs))
    return t.numerator, t.denominator
