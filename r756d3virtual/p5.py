import sys
input = sys.stdin.readline

sys.setrecursionlimit(3*(10**5))
r = int(input())

def dfs(node, ti):
    mint = [-1 for i in range(n+1)]
    q = [(node, ti)]
    seen = {node}
    while q:
        nq = []
        for nd, tk in q:
            #print("Searching", nd, tk)
            if nd != 1 and len(gr[nd]) == 1 and t[nd] > tk:
                return True
            
            for adj in gr[nd]:
                if adj not in seen:
                    seen.add(adj)
                    nq.append((adj, tk+1))
        q = nq

    return False




for _ in range(r):
    input()

    n, k = map(int, input().split())
    gr = dict((i, []) for i in range(1, n+1))

    x = [*map(int, input().split())]
    for i in range(n-1):
        a, b = map(int, input().split())
        gr[a].append(b)
        gr[b].append(a)

    #print(gr)
    t = [0 for i in range(n+1)]
    q = x.copy()
    seen = set(x)
    t0 = 0

    while q:
        nq = []
        for e in q:
            t[e] = t0
            for e2 in gr[e]:
                if e2 not in seen:
                    seen.add(e2)
                    nq.append(e2)

        q = nq

        t0 += 1

    #print(t)

    dfs_seen = {1}
    if dfs(1, 0):
        print("YeS")
    else:
        print("nO")




