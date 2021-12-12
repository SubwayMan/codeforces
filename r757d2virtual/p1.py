import sys
input = sys.stdin.readline

o = []
for _ in range(int(input())):
    n, l, r, k = map(int, input().split())
    a = [*map(int, input().split())]

    tot = 0
    cost = 0
    a.sort()

    for i in a:
        if i < l:
            continue
        elif i > r:
            break
        cost += i
        if cost > k:
            break
        tot += 1
    o.append(tot)
print(*o, sep="\n")
