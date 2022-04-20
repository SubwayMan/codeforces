# virtual contest: Hello 2022
# contest 1621
# written by Tyler Chen
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)[:m]

    ans = ""
    hold = 0
    for i in range(m):
        kn = int(input())
        k = list(map(int, input().split()))
        cval = a[0] * (kn - 1)
        ks = sum(k)
        if ks > a[0] * kn:
            ans = "0" * len(ans)

        if hold != 0:
            ans += "0"*kn
            continue

        for ki in k:
            if ks - ki > cval:
                ans += "0"
            else:
                ans += "1"

        if ks > a[0] * kn:
            hold = 1

    print(ans)
