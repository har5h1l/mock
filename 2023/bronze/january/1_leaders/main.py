# http://usaco.org/index.php?page=viewproblem2&cpid=1275

n = int(input())
breeds = input()
e_vals = [int(i) - 1 for i in input().split()]
ans = 0
first_g = breeds.find('G')
first_h = breeds.find('H')
last_g = breeds.rfind('G')
last_h = breeds.rfind('H')
e_g = e_vals[first_g]
e_h = e_vals[first_h]

if e_g >= last_g:
    if e_h >= last_h:
        ans += 1
    for i in range(n):
        if breeds[i] == 'G':
            continue
        elif i <= first_g and e_vals[i] >= first_g:
            ans += 1
if e_h >= last_h:
    for i in range(n):
        if breeds[i] == 'H':
            continue
        elif i <= first_h and e_vals[i] >= first_h:
            ans += 1

print(ans)