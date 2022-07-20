import sys
input = sys.stdin.readline

t = 1
t = int(input())

def solve():
    a, b, c, x, y = list(map(int, input().split()))
    x = max(0, x-a)
    y = max(0, y-b)
    if c >= x+y:
        print("YES")
        return
    print("NO")


for _ in range(t):
    solve()
