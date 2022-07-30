import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n = int(input())
    d = []
    for i in range(n):
        d.append(tuple(map(int, input().split())))

    s1 = set()
    s2 = set()

    for di in d:
        if di[0] == di[1]:
            print("No")
            return
        if di[0] not in s1 and di[1] not in s1:
            s1.add(di[0])
            s1.add(di[1])
        elif di[0] not in s2 and di[1] not in s2:
            s2.add(di[0])
            s2.add(di[1])
        else:
            print("nO")
            return
    print("YeS")
        

t = 1
t = int(input())

for _ in range(t):
    solve()

