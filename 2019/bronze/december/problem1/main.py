with open('gymnastics.in') as r:
    K, N = map(int, r.readline().split())
    rankings = [list(map(int, ranking.split())) for ranking in r.read().splitlines()]
out = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: continue
        consistent = True
        for ranking in rankings:
            if ranking.index(i) > ranking.index(j):
                consistent = False
                break
        if consistent: out += 1
        

print(out, file = open('gymnastics.out', 'w'))