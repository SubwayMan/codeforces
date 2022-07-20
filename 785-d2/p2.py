import sys
from collections import deque, defaultdict as dd
input = sys.stdin.readline

tt = 1
tt = int(input())

def solve():
    s = input().rstrip()
    ss = set(s)
    rep = len(ss)
    seed = s[:rep]
    if set(seed) != ss:
        print("No")
        return False

    for i in range(rep, len(s), rep):
        if not seed.startswith(s[i:i+rep]):
            print("NO")
            return False
    print("YES")



for _ in range(tt):
    solve()
