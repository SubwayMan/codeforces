import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    maxt = [[0 for i in range(25)] for j in range(m)]

    for i in range(m):
        maxt[i][0] = a[i]

    for j in range(1, 25):
        for i in range(m-(1<<j)+1):
            maxt[i][j] = max(maxt[i][j-1], maxt[i+(1<<(j-1))][j-1])

    q = int(input())

    for _ in range(q):
        yi, xi, yf, xf, k = map(int, input().split())
        if abs(xf-xi)%k != 0 or abs(yf-yi)%k != 0:
            print("NO")
            continue
        apex = yi + k*((n-yi)//k)
        diff = 0
        if xf < xi:
            xi, xf = xf, xi
        xi -= 1
        xf -= 1

        while 1<<(diff+1) <= xf-xi+1:
            diff += 1

        mval = max(maxt[xi][diff], maxt[xf-(1<<diff)+1][diff])
        if apex > mval:
            print("YES")
        else:
            print("NO")


t = 1

for _ in range(t):
    solve()

