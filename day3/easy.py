#!/usr/bin/env python3
from string import digits

s = open("input.txt").read()
s2 = s.split("mul(")[1:]
s3 = [(int(a), "".join(b).split(")")) for a, *b in map(lambda s: s.split(","), s2) if all(map(lambda c: c in digits, a))]
s4 = [a * int(b[0]) for a, b in s3 if all(map(lambda c: c in digits, b[0]))]
print(sum(s4))
