import sys
from math import log
import random
import time
input = sys.stdin.readline


def ans(i):
    return pow((pow(2, i, modval)*m), (n+2*(k-i)), modval)


def f(i):
    p = n + 2*(k - i)
    return i*p + (p / log(2, m))

modval = 998244353
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    a = max(k//2, k//2+1, key=f)
    print(ans(a))



