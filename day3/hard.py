#!/usr/bin/env python3
from string import digits

s = open("input.txt").read()
s1 = [s.split("do()") for s in s.split("don't()")]
s11 = s1[0][0] + "".join(["".join(l[1:]) for l in s1])

s2 = s11.split("mul(")[1:]
s3 = [(int(a), "".join(b).split(")")) for a, *b in map(lambda s: s.split(","), s2) if all(map(lambda c: c in digits, a))]
s4 = [a * int(b[0]) for a, b in s3 if all(map(lambda c: c in digits, b[0]))]
print(sum(s4))
