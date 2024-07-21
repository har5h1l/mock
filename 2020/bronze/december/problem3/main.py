# Stuck In A Rut
# https://usaco.org/index.php?page=viewproblem2&cpid=1061

eastcows = []
northcows = []
n = int(input())
for i in range(n):
    x = input().split()
    if x[0] == 'E': eastcows.append((int(x[1]), int(x[2]), i))
    else: northcows.append((int(x[1]), int(x[2]), i))

out = [float('inf')] * n
eastcows.sort(key = lambda x : x[1])
northcows.sort()

for E in eastcows:
    for N in northcows:
        if N[1] > E[1] or N[0] < E[0] or out[N[2]] != float('inf'): continue
        x_diff = N[0] - E[0]
        y_diff = E[1] - N[1]
        if x_diff > y_diff:
            out[E[2]] = min(x_diff, out[E[2]])
            break
        elif y_diff > x_diff: out[N[2]] = min(y_diff, out[N[2]])

for o in out:
    if o == float('inf'): print('Infinity')
    else: print(o)