import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    k1 = 0
    k2 = 0
    pref1 = [0]
    pref2 = [0]

    for i in range(1, n-1, 2):
        val = (max(0, max(a[i-1], a[i+1]) + 1 - a[i]))
        k1 += val
        pref1.append(pref1[-1] + val)

    if n%2 == 1:
        print(k1)
        return

    for i in range(2, n-1, 2):
        val = (max(0, max(a[i-1], a[i+1]) + 1 - a[i]))
        pref2.append(pref2[-1] + val)

    n2 = len(pref1)
    for i in range(n2):
        k1 = min(k1, pref1[i] + pref2[n2-1] - pref2[i])
    print(k1)




t = 1
t = int(input())

for _ in range(t):
    solve()

