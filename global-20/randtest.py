import random
from itertools import combinations as comb

for _ in range(1):
    n = random.randrange(1, 9)
    a = [random.randrange(1, n+1) for i in range(n)]
    b = a.copy()
    pairs = []

    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                pairs.append((i, j))

    if len(pairs):
        d = random.randrange(len(pairs))
        for i in range(4):
            if d < 3:
                d = random.randrange(len(pairs))

    else:
        d = 0
    random.shuffle(pairs)
    print("a:", a)
    
    print("d", d)
    z = [0 for i in range(n)]
    for i in range(d):
        l, r = pairs[i]
        print("pair", l, r)
        for j in range(l, r-1):
            z[j] += 1
        z[r-1] += l-(r-1)
        print("z:", z)
    for i in range(n):
        b[i] = a[i + z[i]]

    print(b)


dat = "1\n"

