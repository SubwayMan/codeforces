
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())

    a = [*map(int, input().split())]
    a.sort()

    for i in range(1, (n//2)+1):
        print(a[i], a[0])
