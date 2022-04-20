import sys
input = sys.stdin.readline


def maxdist(L, i1, i2):
    return min(i1, i2) + L - max(i1, i2) 


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    lastseen = {}
    maxsum = {}

    for i in range(n):
        if a[i] in lastseen:
            if a[i] in maxsum:
                maxsum[a[i]] = max(maxsum[a[i]], maxdist(n, lastseen[a[i]], i))
            else:
                maxsum[a[i]] = maxdist(n, lastseen[a[i]], i)
        
        lastseen[a[i]] = i

    vals = maxsum.values()
    if len(vals) == 0:
        print(-1)
    else:
        print(max(vals))


