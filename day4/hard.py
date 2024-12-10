#!/usr/bin/env python3

t = open("input.txt").readlines()
# t = open("test.txt").readlines()

def check(r, c):
    if not t[r][c] == 'A':
        return False
    if not ((t[r-1][c-1] == 'M' and t[r+1][c+1] == 'S') or (t[r-1][c-1] == 'S' and t[r+1][c+1] == 'M')):
        return False
    if not ((t[r-1][c+1] == 'M' and t[r+1][c-1] == 'S') or (t[r-1][c+1] == 'S' and t[r+1][c-1] == 'M')):
        return False
    return True

res = 0
for r in range(1, len(t)-1):
    for c in range(1, len(t[0])-1):
        if check(r, c):
            res += 1
print(res)
