# http://www.usaco.org/index.php?page=viewproblem2&cpid=855

r = open('mixmilk.in')

capacities = [0, 0, 0]
measurements = [0, 0, 0]
for i in range(3): capacities[i], measurements[i] = list(map(int, r.readline().split()))

for i in range(100):
    x = i % 3
    y = (x + 1) % 3

    if measurements[x] + measurements[y] > capacities[y]:
        measurements[x] -= capacities[y] - measurements[y]
        measurements[y] = capacities[y]

    else:
        measurements[y] += measurements[x]
        measurements[x] = 0

with open("mixmilk.out", "w") as out:
    for i in range(3): print(measurements[i], file = out)