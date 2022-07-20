import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n = int(input())
    b = list(map(int, input().split()))
    a = [-1 for i in range(n)]
    stack = set(range(1, n+1))
    hold = set()
    for i in range(n, 0, -1):
        if b[i-1] > 0:
            a[i-1] = i//b
            stack.remove(i//b)
            if i in 


t = 1
t = int(input())

for _ in range(t):
    solve()

