# http://www.usaco.org/index.php?page=viewproblem2&cpid=856

r = open('blist.in')

B = [0] * 1000
for _ in range(int(r.readline())):
    s, t, b = list(map(int, r.readline().split()))
    for i in range(s-1, t): B[i] += b

print(max(B), file = open('blist.out', 'w'))