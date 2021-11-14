
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, n = map(int, input().split())
    
    g = n%4
    
    if g==1:
        c = -n
    elif g==2:
        c = 1
    elif g==3:
        c = n+1
    else:
        c = 0

    if x%2:
        c *= -1

    print(x+c)

