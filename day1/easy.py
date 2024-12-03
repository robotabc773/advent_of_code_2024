data = [list(map(int, s.split())) for s in open("input.txt").readlines()]
l1 = [a for a, _ in data]
l2 = [b for _, b in data]
l1.sort()
l2.sort()
res = sum(abs(a - b) for a, b in zip(l1, l2))
print(res)
