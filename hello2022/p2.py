# virtual contest: Hello 2022
# contest 1621
# written by Tyler Chen
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cmax = 0
    cmin = float('inf')
    holds = [0, 0]
    totmax = 0

    for i in range(int(input())):
        l, r, c = map(int, input().split())

        if l <= cmin and r >= cmax:
            totmax = max(totmax, c)
            if r == cmax:
                holds[1] = c
            if l == cmin:
                holds[0] = c

            cmin, cmax = l, r
            

        if l < cmin:
            cmin = l
            holds[0] = c
            totmax = 0
        elif l == cmin:
            holds[0] = min(c, holds[0])

        if r >= cmax:
            cmax = r
            holds[1] = c
        elif r == cmax:
            holds[1] = min(holds[1], c)

        print(sum(holds))






