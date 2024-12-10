#!/usr/bin/env python3
from itertools import product
from operator import add, mul

def comb(a, b):
    return int(str(a) + str(b))

# in_file = "test.txt"
in_file = "input.txt"
eqs = [(int(a), list(map(int, b.split(" ")))) for a, b in [s.split(": ") for s in open(in_file).readlines()]]
res = 0

def test(vs, val, goal, ops):
    if len(vs) == 0:
        return val == goal
    for op in ops:
        new_val = op(val, vs[0])
        if new_val > goal:
            continue
        if test(vs[1:], new_val, goal, ops):
            return True
    return False

for i, (t, vs) in enumerate(eqs):
    print(i, len(eqs))
    if test(vs[1:], vs[0], t, [add, mul, comb]):
        res += t
print(res)
