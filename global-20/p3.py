import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mini = float('inf')
    maxi = -1
    for i in range(1, n):
        if a[i] == a[i-1]:
            mini = min(mini, i-1)
            maxi = max(maxi, i-1)

    if mini > n or maxi == mini:
        print(0)
    elif (maxi - mini == 1):
        print(1)
    else:
        print((maxi - mini) - 1)
