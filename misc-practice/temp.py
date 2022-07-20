import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    bits = [0 for i in range(31)]
    for i in range(n):
        for b in range(31):
            if (1 << b) & a[i]:
                bits[b] += 1
    ans = 0
    for i in range(30, -1, -1):
        if n - bits[i] <= k:
            k -= (n - bits[i])
            ans += 1<<i
    print(ans)
