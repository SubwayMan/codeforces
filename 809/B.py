import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0 for i in range(n)]
    hold = [0 for i in range(n+1)]
    laste = [0 for i in range(n+1)]
    lasto = [0 for i in range(n+1)]

    for i in range(n):
        if i%2 == 0:
            laste[a[i]] = lasto[a[i]] + 1

        else:
            lasto[a[i]] = laste[a[i]] + 1


    for i in range(n):
        ans[i] = max(laste[i+1], lasto[i+1])


    print(*ans)



t = 1
t = int(input())

for _ in range(t):
    solve()

