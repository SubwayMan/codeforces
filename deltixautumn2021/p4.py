import sys
input = sys.stdin.readline

n, d = map(int, input().split())

gr = [{i} for i in range(n+1)]
maxs = 0

for rep in range(1, d+1):
    x, y = map(int, input().split())
    gr[x].add(y)
    gr[y].add(x)
    h = gr[x]|gr[y]
    for i in h:
        gr[i] |= h

    seen = set()
    sizes = []
    etot = rep
    for i in range(1, n+1):
        if i in seen: continue

        seen |= gr[i]
        etot -= (len(gr[i]) - 1)
        sizes.append(len(gr[i]))

    sizes.sort(reverse=True)
    maxn = sizes[0] - 1
    for i in range(1, min(etot, len(sizes)-1) + 1):
        maxn += sizes[i]
    print(maxn)
    
