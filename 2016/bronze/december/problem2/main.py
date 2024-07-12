# https://usaco.org/index.php?page=viewproblem2&cpid=664

out = {
    'a' : 0,
    'b' : 0,
    'c' : 0,
    'd' : 0,
    'e' : 0,
    'f' : 0,
    'g' : 0,
    'h' : 0,
    'i' : 0,
    'j' : 0,
    'k' : 0,
    'l' : 0,
    'm' : 0,
    'n' : 0,
    'o' : 0,
    'p' : 0,
    'q' : 0,
    'r' : 0,
    's' : 0,
    't' : 0,
    'u' : 0,
    'v' : 0,
    'w' : 0,
    'x' : 0,
    'y' : 0,
    'z' : 0,
}

r = open('blocks.in')
for _ in range(int(r.readline())):
    words = r.readline().strip()
    letters = set(words)
    words = words.split()
    for letter in letters:
        if letter != ' ': out[letter] += max(words[0].count(letter), words[1].count(letter))

with open('blocks.out', 'w') as output:
    for o in out.values(): print(o, file = output)