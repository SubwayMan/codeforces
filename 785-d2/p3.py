import sys
from itertools import product
input = sys.stdin.readline

tt = 1
tt = int(input())
modn = 10**9 + 7
plen = 4*10**4 + 1

ans = [0 for i in range(plen)]
ans[0] = 1
kdiff = []

for i in range(1, 6):
    digs = -(-i//2)
    for p in map(tuple, product(range(10), repeat=digs)):
        if p[0] == 0: continue
        d = 0
        for dig in p:
            d = (d+dig) * 10
        z = len(p) - 1
        if (i%2 == 1): z -= 1
        for j in range(z, -1, -1):
            d = (d+p[j]) * 10
        if d//10 < plen:
            kdiff.append(d//10)

for diff in kdiff:
    for rootpos in range(diff):
        if rootpos+diff >= plen:
            break
        for i in range(rootpos+diff, plen, diff):
            ans[i] += ans[i-diff]

def solve():
    n = int(input())
    print(ans[n])

print(kdiff)

for _ in range(tt):
    solve()
