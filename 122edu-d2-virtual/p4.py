import sys
from functools import lru_cache
input = sys.stdin.readline
sys.setrecursionlimit(1001)
t = int(input())


@lru_cache(maxsize=None)
def getcost(e):
    bits = bin(e)
    return len(bits) + bits.count("1") - 4


@lru_cache(maxsize=None)
def dp(i, rem):
    if i == n-1:
        if rem >= getcost(b[i]):
            return c[i]
        return 0

    val = dp(i+1, rem)
    cost = getcost(b[i])
    if cost <= rem:
        val = max(val, dp(i+1, rem-cost) + c[i])
    return val


for _ in range(t):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(dp(0, k))
    dp.cache_clear()
