import sys
input = sys.stdin.readline

t = 1
t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ne = 0
    for i in a:
        if i < 0:
            ne += 1

    for i in range(n):
        a[i] = abs(a[i])
        if i < ne:
            a[i] *= -1
    if sorted(a) == a:
        print("YES")
    else:
        print("NO")



for _ in range(t):
    solve()
