import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    b = [*map(int, input().split())]
    p = [*map(int, input().split())]

    w = [-1 for i in range(n)]
    a = [-1 for i in range(n)]

    for i, e in enumerate(b):
        if e == i+1:
            w[i] = 0
            a[i] = 0
            root = e
            break

    if p[0] != root:
        print(-1)
        continue
    
    wh = 1
    for i in p:

        if i == root:
            continue

        c = w[b[i-1]-1]
        if c< 0:
            print(-1)
            break

        a[i-1] = max(wh, a[b[i-1]-1] + 1)
        wh = a[i-1] + 1
        w[i-1] = a[i-1] - a[b[i-1]-1]

    else:
        print(*w)
        

        






