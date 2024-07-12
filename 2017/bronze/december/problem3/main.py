# https://usaco.org/index.php?page=viewproblem2&cpid=761

def leaderboard(b, e, m): # b -> 0, e -> 1, m -> 2
    score = max(b, e, m)
    out = []
    if b == score: out.append(0)
    if e == score: out.append(1)
    if m == score: out.append(2)
    return out

records = []
r = open('measurement.in')
for _ in range(int(r.readline())): records.append(r.readline().split())
records.sort(key=lambda x: int(x[0]))

records = {}
with open('measurement.in') as r:
    for _ in range(int(r.readline())):
        day, cow, change = r.readline().split()
        records.setdefault(int(day), []).append((cow, int(change)))
    
highest = [0, 1, 2] 
prev_highest = [0, 1, 2]
b, e, m = 7, 7, 7
out = 0
keys = records.keys()

for i in range(1, 101):
    if i not in keys: continue
    for cow, change in records[i]:
        if cow == 'Bessie': b += change
        elif cow == 'Elsie': e += change
        else: m += change
    highest = leaderboard(b, e, m)
    if highest != prev_highest: out += 1
    prev_highest = highest

print(out, file = open('measurement.out', 'w'))