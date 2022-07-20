import sys
input = sys.stdin.readline

t = int(input())

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(max(0, sum(a) - m))


for i in range(t):
    solve()
