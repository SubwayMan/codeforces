import sys
input = sys.stdin.readline

t = 1
# t = int(input())
outp = []


def solve():
    n, m, q = map(int, input().split())
    grid = [0 for i in range(n*m)]
    gset = 0
    for i in range(n):
        col = input().rstrip()
        for j in range(m):
            if col[j] == "*":
                gset += 1
                grid[j*n + i] = 1

    ans = 0
    for i in range(gset):
        ans += grid[i]
    ans = gset-ans

    for _ in range(q):
        x, y = map(int, input().split())
        x, y = x-1, y-1
        pos = y*n + x
        if grid[pos] == 0:
            gset += 1
            if grid[gset-1] == 0:
                ans += 1

            if pos < gset:
                ans -= 1
            grid[pos] = 1

        else:
            gset -= 1
            if grid[gset] == 0:
                ans -= 1

            if pos < gset:
                ans += 1
            grid[pos] = 0

        outp.append(ans)


for _ in range(t):
    solve()

print(*outp, sep="\n")
