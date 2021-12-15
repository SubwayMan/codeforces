import sys
input = sys.stdin.readline

c = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    xneg = list(map(int, input().split()))
    xneg.sort()
    xpos = []

    for e in range(n-1, -1, -1):
        if xneg[e] > 0:
            xpos.append(xneg.pop())
        elif xneg[e] == 0:
            xneg.pop()
        else:
            break

    endp = 0
    dist = 0
    xneg += [0] * (k-(len(xneg)%k))
    xpos += [0] * (k-(len(xpos)%k))

    for i in range(0, len(xneg), k):
        dist += abs(xneg[i]) * 2
        if i==0:
            endp = max(endp, abs(xneg[i]))

    for i in range(0, len(xpos), k):
        dist += xpos[i] * 2
        if i==0:
            endp = max(endp, xpos[i])
    print(dist-endp)

