import sys
import math
from collections import *
from itertools import *
 
input = sys.stdin.readline
 
def solve():
    n, k = map(int, input().split())
    a = set(map(int, input().split()))
    lines = [set() for i in range(3001)]
    for e in a:
        for i in range(1, e+2):
            a1 = e//i 
            if i <= k:
                lines[a1].add(e)
        if e < k:
            lines[0].add(e)
    
    ans = float('inf')
    for lb in range(min(a)+1):
        ts = lines[lb]
        v = 0
        for rb in range(lb+1, 3001):
            if ts == a:
                break
            ts |= lines[rb]
            v += 1
        ans = min(ans, v)
    print(ans)
 
 
 
 
t = 1
t = int(input())
 
for _ in range(t):
    solve()
