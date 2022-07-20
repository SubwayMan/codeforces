import sys
input = sys.stdin.readline

t = 1
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().rstrip()
    p = n//2
    k = s[p]
    ans = 0
    for i in range(p-1, -1, -1):
        if s[i] != k:
            break
        ans += 2
    if n%2 == 1:
        ans += 1
    print(ans)

