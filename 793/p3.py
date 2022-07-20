import sys
from collections import defaultdict as dd
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    kmap = dd(int)

    for e in a:
        kmap[e] += 1
        if kmap[e] > 2:
            n -= 1
    print(-(-n//2))


t = 1
t = int(input())
for _ in range(t):
    solve()
