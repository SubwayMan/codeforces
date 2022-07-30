import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    s = input().rstrip()
    ns = []
    n = len(s)
    lb = n//2 - s.count("(")
    rb = n//2 - s.count(")")
    c = lb
    li = 0
    ri = n
    for i in range(n):
        ch = s[i]
        if ch != "?":
            ns.append(ch)
        else:
            if not c:
                ns.append(")")
                ri = min(ri, i)
            else:
                ns.append("(")
                li = i
                c -= 1

    bf=0
    if lb==0 or rb==0:
        print("YES")
        return
    for i in range(n):
        bf += [-1, 1][ns[i]=="("]
        if li<=i<ri and bf < 2:
            print("YES")
            return
    print("NO")



t = 1
t = int(input())

for _ in range(t):
    solve()

