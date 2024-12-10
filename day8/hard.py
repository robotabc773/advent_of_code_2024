#!/usr/bin/env python3
from itertools import combinations

in_file = "test.txt"
in_file = "input.txt"
m = [list(s.strip()) for s in open(in_file).readlines()]

def in_bounds(pos):
    return pos[0] >= 0 and pos[0] < len(m) and pos[1] >= 0 and pos[1] < len(m[0])

signals : dict[str, set[tuple[int, int]]] = {}
for r, row in enumerate(m):
    for c, char in enumerate(row):
        if char != '.':
            signals[char] = signals.get(char, set()) | {(r, c)}

res = set()
for ants in signals.values():
    for p1, p2 in combinations(ants, 2):
        diff = (p2[0] - p1[0], p2[1] - p1[1])
        n = p1
        while in_bounds(n):
            n = (n[0] - diff[0], n[1] - diff[1])
        n = (n[0] + diff[0], n[1] + diff[1])
        while in_bounds(n):
            res.add(n)
            n = (n[0] + diff[0], n[1] + diff[1])
# print(sorted(list(res)))
print(len(res))
