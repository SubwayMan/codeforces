import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    k = int(input())
    x = list(map(int, input().split()))
    for i in range(3):
        if x[i] == i+1:
            print("NO")
            return
    if x[k-1] == 0:
        print("No")
        return
    print("YES")


t = 1
t = int(input())

for _ in range(t):
    solve()

