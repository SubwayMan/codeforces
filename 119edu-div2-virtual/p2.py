import sys
input = sys.stdin.readline

for _ in range(int(input())):
    w, h = map(int, input().split())

    k, *x = map(int, input().split())
    x.sort()
    x = max(x) - min(x)
    k, *xb = map(int, input().split())
    xb.sort()
    xb = max(xb) - min(xb)

    k, *y = map(int, input().split())
    y.sort()
    y = max(y) - min(y)
    k, *yb = map(int, input().split())
    yb.sort()
    yb = max(yb) - min(yb)


    print(max([xb*h, x*h, y*w, yb*w]))
