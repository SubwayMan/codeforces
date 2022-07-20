import sys
input = sys.stdin.readline

def min_neg(arr):
    n = len(arr)

    mini = n + 1
    maxi = -1
    prod = 1

    for i in range(n):
        if arr[i] < 0:
            mini = min(mini, i)
            maxi = max(maxi, i)
        prod *= arr[i]

    if prod > 0:
        return (prod, 0, 0)

    t1 = 1
    t2 = 1
    for i in range(mini, -1, -1):
        t1 *= arr[i]

    for i in range(maxi, n):
        t2 *= arr[i]

    if abs(t2) > abs(t1):
        return (mini, 0)

    return (n-maxi, 0)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    t = 1
    p0 = []

    for i in range(n):
        t *= a[i]
        if a[i] == 0:
            p0.append(i)
    p0.append(n)

    if t == 0:
        ind = 0
        hprod, hu, hv = 0, 0, 0
        for i in p0:
            prod, u, v = min_neg(a[ind:i])
            if prod > hprod:
                hprod, hu, hv = prod, u, v
            ind = i+1
        

        print(0, 0)

