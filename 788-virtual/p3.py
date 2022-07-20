import sys
input = sys.stdin.readline

t = 1
t = int(input())
out = []
mod = 10**9 + 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = list(map(int, input().split()))
    aw = [0 for i in range(n+1)]
    for i in range(n):
        aw[a[i]] = i

    seen = set()
    for i in range(n):
        if d[i]:
            seen.add(a[i])
            seen.add(b[i])
    
    ans = 1
    for i in range(n):
        if a[i] in seen:
            continue
        nxt = b[i]
        seen.add(b[i])

        cl = 1
        while a[i] != nxt:
            nxt = b[aw[nxt]]
            if nxt in seen:
                cl = 1
                break
            seen.add(nxt)

            cl = 2
        ans = (ans*cl) % mod
    out.append(ans)


for _ in range(t):
    solve()

print(*out, sep="\n")
