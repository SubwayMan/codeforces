import sys
input = sys.stdin.readline
from math import log

t = 1
t = int(input())

def solve():
    x, y = map(int, input().split())
    z = y/x
    if int(z) != z:
        print(0, 0)
        return
    z = int(z)
    print(1, z)


for _ in range(t):
    solve()
