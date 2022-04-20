import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    a = [0 for i in range(n)]

    aval = sum(h)//n
    for i in range(n-1, 1, -1):
        if h[i] + a[i] < aval:
            continue

        d = min(h[i] // 3, (h[i] + a[i] - aval) // 3)
        a[i-1] += d
        a[i-2] += d * 2
        a[i] -= d * 3
    
    print(a)
    for i in range(n-1, -1, -1):
        h[i] += a[i]

    print(min(h))

