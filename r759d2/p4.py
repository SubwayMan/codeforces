import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print("yEs")
        continue

    p = sorted(a)

    for i in range(n):
        if a[i] != p[i]:
