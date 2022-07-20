import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def canfit(n, fmap, k, tasks):
    time = k*n
    z = [k for i in range(n)]
    for i in range(n):
        z[i] -= min(k, fmap[i+1])
        tasks -= min(k, fmap[i+1])
    s = 0
    for i in z:
        s += i//2
    return s >= tasks



def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    tot = 0
    fmap = [0 for i in range(n+1)]
    for i in a:
        fmap[i] += 1
        tot += 1

    tm = 0
    diff = n
    while (diff):
        while not canfit(n, fmap, diff+tm, tot):
            tm += diff
        diff //= 2
    print(tm+1)

t = 1
t = int(input())

for _ in range(t):
    solve()

