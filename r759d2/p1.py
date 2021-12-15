import sys
input = sys.stdin.readline

c = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    t = 1
    if a[0]:
        t += 1
    for i in range(1, n):
        if a[i]:
            if a[i-1]:
                t += 5
            else:
                t += 1
        else:
            if not a[i-1]:
                c.append(-1)
                break
    else:
        c.append(t)

print(*c, sep="\n")
