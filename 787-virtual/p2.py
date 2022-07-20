import sys
from math import log
input = sys.stdin.readline

t = 1
t = int(input())
al = []


def tr(n):
    return "0" + bin(n)[2:]


def solve():
    n = int(input())
    a = [tr(i) for i in map(int, input().split())]
    ans = 0
    for i in range(n-2, -1, -1):
        if a[i+1] == "0":
            ans = -1
            break
        
        li = len(a[i])
        ln = len(a[i+1])

        if li < ln:
            continue
        elif li == ln and a[i] < a[i+1]:
            continue

        f = li - ln

        a[i] = a[i][:ln]
        if a[i] >= a[i+1]:
            a[i] = a[i][:-1]
            f += 1
        ans += f

    al.append(ans)

for _ in range(t):
    solve()
print(*al, sep="\n")
