import sys
from collections import deque, defaultdict as dd
input = sys.stdin.readline

tt = 1
tt = int(input())


def solve():
    s = input().rstrip()
    ans = 0
    for ch in s:
        ans += ord(ch) - ord('a') + 1
    if len(s) % 2 == 0:
        print("Alice", ans)
        return
    b = min(ord(s[0]) - 96, ord(s[-1]) - 96)
    ans -= b
    if b > ans:
        print("Bob", b-ans)
    else:
        print("Alice", ans-b)


for _ in range(tt):
    solve()
