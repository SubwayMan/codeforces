import sys
input = sys.stdin.readline

t = int(input())
tot = 0

def xor_tree(n, par):
    c = gr[n]
    ret =   m[n-1] 
    for k in c:
        if k==par:
            continue
        ret ^= xor_tree(k, n)
    xo[n-1] = ret
    return xo[n-1]

def findn(i, n, par):
    global tot
    c = gr[n]
    ret = xo[n-1]

    for k in c:
        if k==par: continue
        if xo[k-1] == par:
            tot += 1
        else:
            findn(i, k, n)


for _ in range(t):
    n, k = map(int, input().split())
    m = [*map(int, input().split())]
    xo = [0 for i in range(n)]
    gr = dict((i, []) for i in range(1, n+1))
    tot = 0

    for i in range(n-1):
        n1, n2 = map(int, input().split())
        gr[n1].append(n2)
        gr[n2].append(n1)

    xtot = 0
    for i in m:
        xtot ^= i

    if xtot==0:
        print("yEs")
        continue
    else:
        xor_tree(1, 0)
        findn(xtot, 1, 0)
        if tot >= 2:
            print("yES")
        else:
            print("nO")

