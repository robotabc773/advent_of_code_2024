#!/usr/bin/env python3
print(sum(u[len(u)//2] for u in [list(map(int, u.split(","))) for u in open("input.txt").read().split("\n\n")[1].strip().split("\n")] if u == sorted(u, key=lambda n: len(list(filter(lambda r: r[1] == n and r[0] in u, [list(map(int, r.split("|"))) for r in open("input.txt").read().split("\n\n")[0].split("\n")]))))))
