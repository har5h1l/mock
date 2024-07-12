# http://www.usaco.org/index.php?page=viewproblem2&cpid=568

r = open('speeding.in')

n, m = list(map(int, r.readline().split()))

limits = [0]
speeds = [0]

for _ in range(n):
    a, b = list(map(int, r.readline().split()))
    for _ in range(limits[-1], limits[-1] + a): limits.append(b)

for _ in range(m):
    a, b = list(map(int, r.readline().split()))
    for _ in range(speeds[-1], speeds[-1] + a): speeds.append(b)
    
maxspeed = 0
for i in range(1, 101): maxspeed = max(maxspeed, speeds[i] - limits[i])

print(maxspeed, file = open('speeding.out', 'w'))