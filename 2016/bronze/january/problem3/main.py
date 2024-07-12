# https://usaco.org/index.php?page=viewproblem2&cpid=593

r = open('mowing.in')
x, y, t = 0, 0, 0
visited = dict() # (x, y, t)
max_speed = float('inf')

for _ in range(int(r.readline().strip())):
    direction, units = r.readline().strip().split()
    if direction == 'N':
        for _ in range(int(units)):
            t += 1
            y += 1
            if (x, y) in visited.keys():
                max_speed = min(t - visited[(x, y)], max_speed)
            visited[(x, y)] = t
    elif direction == 'E':
        for _ in range(int(units)):
            t += 1
            x += 1
            if (x, y) in visited.keys(): max_speed = min(t - visited[(x, y)], max_speed)
            visited[(x, y)] = t
    elif direction == 'S':
        for _ in range(int(units)):
            t += 1
            y -= 1
            if (x, y) in visited.keys(): max_speed = min(t - visited[(x, y)], max_speed)
            visited[(x, y)] = t
    elif direction == 'W':
        for _ in range(int(units)):
            t += 1
            x -= 1
            if (x, y) in visited.keys(): max_speed = min(t - visited[(x, y)], max_speed)
            visited[(x, y)] = t
if max_speed == float('inf'): max_speed = -1

print(max_speed, file = open('mowing.out', 'w'))
