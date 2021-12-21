import sys
from collections import defaultdict as dd
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    gmap = {}
    tmap = []
    xmap = dd(list)
    ymap = dd(list)

    for i in range(n):
        x, y, t = map(int, input().split())
        for adj in xmap[x]:
            if abs(adj[1] - y) <= k:
                gmap[(x, y)] = gmap[adj]
                tmap[gmap[(x, y)]] = min(tmap[gmap[(x, y)]], t)
                break
        else:
            for adj in ymap[y]:
                if abs(adj[0] - x) <= k:
                    gmap[(x, y)] = gmap[adj]
                    tmap[gmap[(x, y)]] = min(tmap[gmap[(x, y)]], t)
                    break
            else:
                gmap[(x, y)] = len(tmap)
                tmap.append(t)
                xmap[x].append((x, y))
                ymap[y].append((x, y))

    tmap.sort()
    print(tmap)
    print(sum(tmap[:-(-len(tmap)//2)]))

