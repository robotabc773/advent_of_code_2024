#!/usr/bin/env python3

m = [list(l.strip()) for l in open("input.txt").readlines()]

start_pos = (0, 0)
for r, row in enumerate(m):
    for c, char in enumerate(row):
        if m[r][c] == '^':
            start_pos = (r, c)
            break
rotate = {
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1),
    (0, -1): (-1, 0)
}

def in_bounds(pos):
    return pos[0] >= 0 and pos[0] < len(m) and pos[1] >= 0 and pos[1] < len(m[0])

res = 0
for r in range(len(m)):
    for c in range(len(m[0])):
        if m[r][c] == '.':
            m[r][c] = '#'
            pos = start_pos
            dir  = (-1, 0)
            visited = {(pos, dir)}
            print(r, c)
            while True:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if not in_bounds(new_pos):
                    m[r][c] = '.'
                    break
                if m[new_pos[0]][new_pos[1]] == '#':
                    dir = rotate[dir]
                else:
                    pos = new_pos
                if (pos, dir) in visited:
                    res += 1
                    m[r][c] = '.'
                    break
                visited.add((pos, dir))
print(res)
