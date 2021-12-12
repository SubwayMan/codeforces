import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, h = map(int, input().split())
    gaps = []
    a = [*map(int, input().split())]

    for i in range(1, n):
        gaps.append(a[i] - a[i-1])

    gaps.sort()
    ma = 0
    dmg = 0

    for i, g in enumerate(gaps):

        left = h - (dmg + ma)
        dpot = (-(-left//(n-i)))+ma
        if dpot <= g:
            print(dpot)
            break

        dmg += (g-ma)*(n-(i+1))

        if g > ma:
            ma = g

    else:
        print(h-dmg)
        
     
