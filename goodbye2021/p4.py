import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    ans = 0
    ja = []
    for i in range(n):
        if a[i] >= k:
            ans += 1
        else:
            ja.append(a[i], i)

    ja.sort()
