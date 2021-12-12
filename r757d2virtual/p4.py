import sys
from math import gcd
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    a.sort(reverse=True)

    checked = [-1 for i in range(n)]
    

