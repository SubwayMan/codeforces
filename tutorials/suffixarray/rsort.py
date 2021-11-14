
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

c = [(3, 2), (2, 1), (1, 3), (0, 1), (2, 0), (3, 0), (1, 2), (3, 1)]
print(radix_sort(c))
