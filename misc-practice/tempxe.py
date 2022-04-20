import sys
from math import log
from random import randrange
input = sys.stdin.readline


def f(i):
    if i < 0 or i > k:
        return 0

    p = n + 2*(k - i)
    return i*p + (p / log(2, m))


def ans(i):
    return pow((pow(2, i, modval)*m), (n+2*(k-i)), modval)


modval = 998244353
for _ in range(int(input())):
    m, n, k = randrange(10**8, 10**9), randrange(10**8, 10**9), randrange(10**11, 10**12)
    lb = 0
    rb = k
    lastmid = -1
    while True:
        mid = (lb + rb) // 2

        mf = f(mid)
        c = mid-1
        while f(c) == mf:
            c -= 1
        d = mid + 1
        while f(d) == mf:
            d += 1

        if f(d) > mf:
            lb = mid
        elif f(c) > mf:
            rb = mid
        else:
            print(m, n, k)
            print(mid, k//2)
            break

