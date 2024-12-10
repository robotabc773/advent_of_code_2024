#!/usr/bin/env python3

t = open("input.txt").readlines()
# t = open("test.txt").readlines()

def check(r, c, dr, dc):
    if r + 3 * dr < 0 or c + 3 * dc < 0:
        return False
    if r + 3 * dr >= len(t) or c + 3 * dc >= len(t[0]):
        return False
    return t[r][c] == 'X' and \
            t[r + dr][c + dc] == 'M' and \
            t[r + 2 * dr][c + 2 * dc] == 'A' and \
            t[r + 3 * dr][c + 3 * dc] == 'S'

deltas = [(dr, dc) for dr in range(-1,2) for dc in range(-1,2) if not (dr == 0 and dc == 0)]
print(deltas)
res = 0
for r in range(len(t)):
    for c in range(len(t[0])):
        for dr, dc in deltas:
            if check(r, c, dr, dc):
                res += 1
print(res)
