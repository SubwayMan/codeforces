import sys
input = sys.stdin.readline

a = []
for _ in range(int(input())):
    n = int(input())
    k = [*map(int, input().split())]
    k.sort()
    ma=k[0]
    diff = -k[0]

    for i in range(1, n):
        f = k[i]+diff
        ma = max(f, ma)
        diff -= f

    a.append(ma)

print(*a, sep="\n")
