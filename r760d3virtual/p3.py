import sys
from math import gcd
input = sys.stdin.readline 

def lcm(li):
    f = li[0]
    for i in li[1:]:
        f = (f*i)//gcd(f, i)
    return f

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    g1 = a[0]
    for i in a[::2]:
        g1 = gcd(g1, i)

    g2 = a[1]
    for i in a[1::2]:
        if i % g1 == 0:
            g1 //= gcd(g1, i)

        g2 = gcd(g2, i)


    for i in a[::2]:
        if i%g2 == 0:
            g2 //= gcd(g2, i)

    if g1 != 1:
        print(g1)
    elif g2 != 1:
        print(g2)
    else:
        print(0)
