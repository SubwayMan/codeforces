import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n):
        if a[i]%a[0] != 0:
            print("NO")
            return
    print("YES")

t = 1
t = int(input())

for _ in range(t):
    solve()

