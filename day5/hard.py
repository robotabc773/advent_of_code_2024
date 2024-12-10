#!/usr/bin/env python3
raw = open("input.txt").read().split("\n\n")
rules = [list(map(int, r.split("|"))) for r in raw[0].split("\n")]
updates = [list(map(int, u.split(","))) for u in raw[1].strip().split("\n")]

fixed = [sorted(u, key=lambda n: len(list(filter(lambda r: r[1] == n and r[0] in u, rules)))) for u in updates]
res = sum(f[len(u)//2] for u, f in zip(updates, fixed) if u != f)
print(res)
