import sys
input = sys.stdin.readline

vals = []
for _ in range(int(input())):
    n, a, b = map(int, input().split())
    x = list(map(int, input().split()))
    pos = 0
    ans = 0
    for e in range(n):
        i = x[e]
        ans += (i-pos) * b
        if (a < b*(n-e-1)) and e != n-1:
            ans += (i-pos) * a
            pos = i

    vals.append(ans)

print(*vals, sep="\n")
