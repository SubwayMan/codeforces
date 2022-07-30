import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    diffs = []
    ndiffs = []
    for i in range(1, n):
        diffs.append(max(a[i]-a[i-1], 0))
        ndiffs.append(max(a[i-1]-a[i], 0))
    pre1 = [0]
    pre2 = [0]
    for i in range(n-1):
        pre1.append(pre1[-1]+diffs[i])
        pre2.append(pre2[-1]+ndiffs[i])

    for i in range(m):
        s, t = map(int, input().split())

        if s<t:
            print(pre2[t-1]-pre2[s-1])
        else:
            print(pre1[s-1]-pre1[t-1])

t = 1

for _ in range(t):
    solve()

