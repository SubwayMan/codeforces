import sys
input = sys.stdin.readline
ans = []
t = int(input())
for ty in range(t):
    c = input()
    k = [*map(int, input().strip().split())]

    d = [k]
    while True:
        a = []
        for ch in k:
            a.append(k.count(ch))
        k = a
        if d[-1]==k: break
        d.append(k)
    q = int(input())
    for _ in range(q):
        xi, ki = map(int, input().split())
        if ki>=len(d):
            ans.append(d[-1][xi-1])
        else:
            ans.append(d[ki][xi-1])

print(*ans, sep="\n")


