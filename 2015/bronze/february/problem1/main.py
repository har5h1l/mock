# https://usaco.org/index.php?page=viewproblem2&cpid=526

r = open('censor.in')
S = r.readline().strip()
t = r.readline().strip()
x = - len(t)
out = ''

for s in S:
    out += s
    if out[x:] == t: out = out[:x]

print(out, file = open('censor.out', 'w'))