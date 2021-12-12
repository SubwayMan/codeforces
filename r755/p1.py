import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    u, v = map(int, input().split())

    print(-u, v)
