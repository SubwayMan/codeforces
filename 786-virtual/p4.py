import sys
input = sys.stdin.readline

t = 1
t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    c = []
    e = 0
    if n%2 == 1:
        c.append(a[0])
        e = 1

    for i in range(e, n, 2):
        c.append(a[i])
        c.append(a[i+1])
        if a[i+1] < a[i]:
            c[-1], c[-2] = c[-2], c[-1]

    for i in range(1, n):
        if c[i] < c[i-1]:
            print("NO")
            return
    print("YES")

for _ in range(t):
    solve()
