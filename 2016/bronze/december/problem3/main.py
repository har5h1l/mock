# http://www.usaco.org/index.php?page=viewproblem2&cpid=665

r = open('cowsignal.in')

m, n, k = list(map(int, r.readline().split()))
out = ''

for _ in range(m):
    out += (''.join([k * i for i in r.readline().strip()]) + '\n') * k

print(out, end='', file=open('cowsignal.out', 'w'))