from collections import Counter

data = [list(map(int, s.split())) for s in open("input.txt").readlines()]
l1 = Counter([a for a, _ in data])
l2 = Counter([b for _, b in data])
res = 0
for n in l1.keys():
    res += l1[n] * l2[n] * n
print(res)
