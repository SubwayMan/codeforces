import sys
input = sys.stdin.readline

vals = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [1 for i in range(n)]
    for i in range(n):
        if a[i] == 0:
            ans[i] = 0
            continue

        if ans[i] != 0:
            if a[i] < n:
                ans[a[i]] = 0

        elif a[i] < n - i:
            ans[a[i] + i] = 0
    print(*ans)

