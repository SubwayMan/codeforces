import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    c = 0
    a = sorted([*map(int, input().split())])

    for i in range(n):
        while not a[i]&1:
            a[i] >>= 1
            c += 1
    print((sum(a[:n])-max(a)) + (max(a)<<c))

