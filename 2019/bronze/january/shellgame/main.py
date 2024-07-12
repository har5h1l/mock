# http://www.usaco.org/index.php?page=viewproblem2&cpid=891 

r = open('shell.in')

n = int(r.readline())

shells = [0, 1, 2]
picks = [0, 0, 0]

for _ in range(n):
    a, b, g = list(map(lambda x: int(x) - 1, r.readline().split()))
    shells[a], shells[b] = shells[b], shells[a]
    picks[shells[g]] += 1

print(max(picks), file = open('shell.out', 'w'))