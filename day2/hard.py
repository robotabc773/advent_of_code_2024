#!/usr/bin/env python3

reps = [list(map(int, l.split())) for l in open("input.txt").readlines()]

res = 0
for rep in reps:
    diffs = [b - a for b, a in zip(rep[:-1], rep[1:])]
    if (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)) and all(abs(d) <= 3 for d in diffs):
        res += 1
    else:
        good = False
        for i in range(len(rep)):
            rep2 = rep.copy()
            rep2.pop(i)
            diffs = [b - a for b, a in zip(rep2[:-1], rep2[1:])]
            if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
                if all(abs(d) <= 3 for d in diffs):
                    good = True
                    break
        if good:
            res += 1
print(res)
