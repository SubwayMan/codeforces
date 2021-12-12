
import sys
input = sys.stdin.readline

ans = []
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    p = (max(a,b) - min(a,b))//2
    if p > min(a, b):
        p = min(a, b)

    ans.append(p + (min(a,b)-p)//2)

print(*ans, sep="\n")
