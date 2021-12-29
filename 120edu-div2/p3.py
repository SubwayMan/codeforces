import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    tot = sum(a) - (len(a) * a[0])
    osum = sum(a)

    ans = max(0, osum - k)

    if n==1:
        print(ans)
        continue

    for i in range(1, n):
        tot -= a[i-1] - a[0]
        gsize = n-i
        rdist = (osum-tot)-k

        f = gsize
        if rdist > 0:
            f += -(-rdist//(gsize + 1))

        ans = min(ans, f)

    print(ans)

