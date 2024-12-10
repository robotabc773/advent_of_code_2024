#!/usr/bin/env python3

m = [l.strip() for l in open("input.txt").readlines()]

pos = (0, 0)
for r, row in enumerate(m):
    for c, char in enumerate(row):
        if m[r][c] == '^':
            pos = (r, c)
            break
visited = {pos}
dir = (-1, 0)
rotate = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

def in_bounds(pos):
    return pos[0] >= 0 and pos[0] < len(m) and pos[1] >= 0 and pos[1] < len(m[0])

while in_bounds(pos):
    new_pos = (pos[0] + dir[0], pos[1] + dir[1])
    if in_bounds(new_pos) and m[new_pos[0]][new_pos[1]] == '#':
        dir = rotate[dir]
    else:
        pos = new_pos
        if in_bounds(new_pos):
            visited.add(pos)
        print(pos)
print(len(visited))
