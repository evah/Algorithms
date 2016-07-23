##Compare a, b two strings to see if they are the permutation of each other, complexity O(n)

import collections

def same_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return not any(d.itervalues())
