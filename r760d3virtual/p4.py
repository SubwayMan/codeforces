import sys
input = sys.stdin.readline 

for _ in range(int(input())):
    n, k = map(int, input().split())

    a = sorted(map(int, input().split()), reverse=True)
    f = sum(a)
    g = a[:k*2]
    if len(g)%2:
        g = g[:-1]

    for i in set(g):
        if g.count(i) > len(g)//2:
            f += (g.count(i) - (len(g)//2))
    f -= sum(g)
    print(f)



