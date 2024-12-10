#!/usr/bin/env python3
from itertools import product
from operator import add, mul

# in_file = "test.txt"
in_file = "input.txt"
eqs = [(int(a), list(map(int, b.split(" ")))) for a, b in [s.split(": ") for s in open(in_file).readlines()]]
res = 0
for t, vs in eqs:
    for ops in product([add, mul], repeat=len(vs)-1):
        val = vs[0]
        for v, op in zip(vs[1:], ops):
            val = op(val, v)
        if val == t:
            res += t
            break
print(res)
