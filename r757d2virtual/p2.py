import sys
input = sys.stdin.readline

o = []
for _ in range(int(input())):
    n = int(input())
    a = [*map(int, input().split())]
    b = sorted(range(n), key=lambda k: a[k], reverse=True)
    c = [-1 for i in range(n)]

    v = 1
    for i in b:
        c[i] = v
        if v > 0:
            v = -v
        else:
            v = abs(v) + 1
    
    print(sum([a[i]*2*abs(c[i]) for i in range(n)]))
    print(0, *c)

