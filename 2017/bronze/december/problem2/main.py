# http://www.usaco.org/index.php?page=viewproblem2&cpid=760

r = open('shuffle.in')

N = int(r.readline().split()[0])
shuffle = list(map(int, r.readline().split()))
positions = r.readline().split()

for _ in range(3): positions = [positions[shuffle[i] - 1] for i in range(N)]

print('\n'.join(positions), file = open('shuffle.out', 'w'))