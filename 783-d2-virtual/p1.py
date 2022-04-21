import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n == 1:
        if m > 2:
            print(-1)
            continue
        else:
            print(m-1)
            continue
    if m == 1:
        if n > 2:
            print(-1)
            continue
        else:
            print(n-1)
            continue

    ans = (min(n, m) - 1) * 2
    rem = max(n, m) - min(n, m)
    ans += rem + 2 * (rem//2)
    print(ans)
