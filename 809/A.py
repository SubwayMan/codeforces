import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = ["B"] * m
    for i in range(n):
        u1, u2 = a[i] - 1, m - a[i]
        if u1<u2:
            u1, u2 = u2, u1
        if b[u2] != "A":
            b[u2] = "A"
        else:
            b[u1] = "A"
    print("".join(b))


t = 1
t = int(input())

for _ in range(t):
    solve()

