# http://www.usaco.org/index.php?page=viewproblem2&cpid=735

x, y = list(map(int, open('lostcow.in').readline().split()))

location = x
traveled = 0

i = 1 # offset
while location != y:
    if i > 0: location += 1
    else: location -= 1
    traveled += 1

    if location == x + i: i *= -2

print(traveled, file = open('lostcow.out', 'w'))