import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n = int(input())
    ans = []
    seen = set()

    for i in range(1, n+1):
        if i in seen:
            continue
        c = i
        ans.append(i)
        while c*2 <= n:
            c *= 2
            if c in seen: break
            seen.add(c)
            ans.append(c)
    print(2)
    print(*ans)


t = 1
t = int(input())

for _ in range(t):
    solve()

