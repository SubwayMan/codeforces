import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    ans = ""
    iq = 0
    for i in range(n-1, -1, -1):
        if a[i] > iq:
            if iq < q:
                ans = "1" + ans
                iq += 1
            else:
                ans = "0" + ans
        else:
            ans = "1" + ans
    print(ans)

t = 1
t = int(input())

for _ in range(t):
    solve()

