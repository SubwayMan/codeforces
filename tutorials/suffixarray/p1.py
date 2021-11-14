c = input() + "$"
n = len(c)

k = 1

while k//2 < n:
   
    if k==1:
        a = [(c[i], i) for i in range(n)]

    else:
        a = [((eq[i], eq[(i+k//2)%n]), i) for i in range(n)]

    a.sort()
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

   


