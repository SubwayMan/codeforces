import sys
input = sys.stdin.readline


out = []

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    k = []
    for i in range(n):
        if a[i] != i:
            k.append(a[i])

    ans = k[0]
    for i in range(1, len(k)):
        ans &= k[i]
    out.append(ans)


t = 1
t = int(input())
for _ in range(t):
    solve()

print(*out, sep="\n")
