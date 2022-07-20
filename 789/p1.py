import sys
input = sys.stdin.readline

t = 1
t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    d = a.count(0)

    if d != 0:
        print(n-d)
        return

    if len(set(a)) == len(a):
        print(n+1)
    else:
        print(n)



for _ in range(t):
    solve()
