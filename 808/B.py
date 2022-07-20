import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n, l, r = map(int, input().split())
    ans = []
    for i in range(1, n+1):
        lb = (l//i)*i
        rb = (l//i+1) * i
        if lb < l and rb > r:
            print("NO")
            return
        if lb >= l:
            ans.append(lb)
        else:
            ans.append(lb+i)
    print("YES")
    print(*ans)


t = 1
t = int(input())

for _ in range(t):
    solve()

