import sys
import math
from collections import *
from itertools import *

input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    s = input().rstrip()
    ans = 0
    if s.count("1") == 0:
        print(0)
        return 

    for i in range(n-1):
        ans += int(s[i:i+2])

    rb = 0
    for i in range(n-1, -1, -1):
        if s[i] == "1":
            rb = n-1-i
            break

    lb = 0
    for i in range(n):
        if s[i] == "1":
            lb = i
            break
    

    if k >= rb:
        if rb > 0:
            ans -= 10
            k -= rb
        if s.count("1") == 1:
            if s[0] == "1":
                ans += 1

            print(ans)
            return

    if k>=lb>0:
        ans -= 1
    print(ans)


t = 1
t = int(input())

for _ in range(t):
    solve()

