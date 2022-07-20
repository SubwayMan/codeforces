import sys
input = sys.stdin.readline

t = 1
t = int(input())
aa = []

def solve():
    n = int(input())
    s = list(input().rstrip())
    s.append("#")

    c = 1
    ans = 0
    lens = []

    for i in range(1, n+1):
        if s[i] != s[i-1]:
            lens.append(c)
            c = 1
        else:
            c += 1
    nlens = len(lens) 
    segs = [0 for i in range(nlens+1)]
    segs[:2] = [1, 1]
    stot = lens[0]
    print(lens)
    for i in range(2, nlens+1):
        segs[i] = segs[i-1] + 1

        if lens[i-2] == 1:
            segs[i] = min(segs[i], segs[i-2])

        if lens[i-1] == 1:
            segs[i] = min(segs[i], segs[i-1])

        if stot%2 == 1 and lens[i-2] == 2:
            segs[i] = min(segs[i], segs[i-2])

        stot += lens[i-1]
    print(segs)

    for i in range(len(lens) - 1):
        if lens[i] % 2 == 1:
            ans += 1
            lens[i+1] += 1
            lens[i] -= 1

    print(ans, segs[-1])

for _ in range(t):
    solve()

