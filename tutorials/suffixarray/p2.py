c = input() + "$"
n = len(c)

def radix_sort(f):
    n = len(f)
    for g in range(1, -1, -1):
        b = [0 for i in range(n)]
        for i in f:
            b[i[g]] += 1
        p = [0 for i in range(n)]
        for i in range(1, n):
            if not b[i-1]: break
            p[i] = p[i-1]+b[i-1]

        l = [0 for i in range(n)]
        for i in range(n):

            l[p[f[i][g]]] = f[i]
            p[f[i][g]] += 1
        f = l
    return f

k = 1

while k//2 < n:
   
    if k==1:
        a = [(c[i], i) for i in range(n)]
        a.sort()

    else:
        a = radix_sort([((eq[i], eq[(i+k//2)%n]), i) for i in range(n)])

    p = [j[1] for j in a]

    eq = [-1 for i in range(n)]
    eq[p[0]] = 0

    ei = 0
    fl = True
    for pi in range(1,n):
        ch, ind = a[pi]
        if ch != a[pi-1][0]:
            ei += 1
        else:
            fl = False
        eq[ind] = ei

    if fl:
        print(*p)
        break

    k <<= 1

   


