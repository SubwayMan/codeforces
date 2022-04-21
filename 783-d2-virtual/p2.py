import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    c = sorted(map(int, input().split()), reverse=True)

    ans = c[0] * 2 + 1
    for i in range(1, n):
        ans += 1
        if i != n-1:
            ans += c[i]
    if ans <= m:
        print("YeS")
    else:
        print("nO")
