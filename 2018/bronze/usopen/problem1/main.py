# https://usaco.org/index.php?page=viewproblem2&cpid=831

r = open('tttt.in')
ttt = []
for _ in range(3): ttt += list(r.readline().strip())
out1 = 0
out2 = 0

combinations = {tuple(sorted(set(ttt[0:3]))), tuple(sorted(set(ttt[3:6]))), tuple(sorted(set(ttt[6:]))), tuple(sorted({ttt[0], ttt[3], ttt[6]})), tuple(sorted({ttt[1], ttt[4], ttt[7]})), tuple(sorted({ttt[2], ttt[5], ttt[8]})), tuple(sorted({ttt[0], ttt[4], ttt[8]})), tuple(sorted({ttt[2], ttt[4], ttt[6]}))}

for c in combinations:
    if len(c) == 1: out1 += 1
    elif len(c) == 2: out2 += 1

print(str(out1) + '\n' + str(out2), file = open('tttt.out', 'w'))