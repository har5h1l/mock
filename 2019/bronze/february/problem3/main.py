# http://www.usaco.org/index.php?page=viewproblem2&cpid=917

r = open('traffic.in')

traffic = []
for _ in range(int(r.readline())):
    x = r.readline().split()
    x[1], x[2] = int(x[1]), int(x[2])
    traffic.append(x)

# start
A, B = 0, 1000
for htype, a, b in reversed(traffic):
    if htype == 'none': A, B = max(A, a), min(B, b)
    elif htype == 'off':
        A += a
        B += b
    else:
        A -= b
        B -= a
        if A < 0: A = 0

startout = f"{A} {B}"

# end
A, B = 0, 1000
for htype, a, b in traffic:
    if htype == 'none': A, B = max(A, a), min(B, b)
    elif htype == 'on':
        A += a
        B += b
    else:
        A -= b
        B -= a
        if A < 0: A = 0

print(f"{startout}\n{A} {B}", file = open('traffic.out', 'w'))