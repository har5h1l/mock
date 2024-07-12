# http://www.usaco.org/index.php?page=viewproblem2&cpid=616 

f = open('cbarn.in')
n = int(f.readline())
R = list(map(int, f.readlines()))

out = sum(R) * n
for i in range(n): out = min(out, sum([R[j % n] * (j-i) for j in range(i+1, n+i)]))
print(out, file = open('cbarn.out', 'w'))