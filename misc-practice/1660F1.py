import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().rstrip()
    pl = [0]
    mi = [0]
    for i in range(n):
        pl.append(pl[-1])
        mi.append(mi[-1])
        if s[i] == "+":
            pl[-1] += 1
        else:
            mi[-1] += 1
    ans = 0
    for i in range(n):
        for j in range(i+1, n+1):
            np = pl[j] - pl[i]
            nm = mi[j] - mi[i]
            if nm >= np and (nm-np)%3 == 0:
                ans  += 1
    print(ans)

t = 1
t = int(input())

for _ in range(t):
    solve()

