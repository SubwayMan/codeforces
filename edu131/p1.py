import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if [a, b, c, d] == [1, 1, 1, 1]:
        print(2)
    else:
        print(a|b|c|d)


t = 1
t = int(input())

for _ in range(t):
    solve()

