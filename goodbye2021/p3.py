import sys
from fractions import Fraction
from collections import Counter

input = sys.stdin.readline


def check(arr):

    if len(arr) <= 2:
        return 0
    
    cc = Counter()

    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            frac = Fraction(arr[j]-arr[i], j-i)
            cc[(arr[i] - (frac*i), frac)] += 1

    ans = float('inf')
    ind, d = cc.most_common(1)[0][0]
    a = 0
    for i in range(0, len(arr)):
        if arr[i] != (ind + d*(i)):
            a += 1

    ans = min(ans, a)

    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(check(a))

