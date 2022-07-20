import sys
input = sys.stdin.readline

t = 1
t = int(input())
ans = []

def solve():
    n = int(input())
    s = input().rstrip()
    k, *ch = input().split()
    ch = set(ch)
    la = 0
    for i in range(n):
        if s[i] in ch:
            la = i
    
    m = la
    lst = 0
    maxd = 0
    for i in range(m+1):
        if s[i] in ch:
            maxd = max(maxd, i-lst)
            la = max(la-(i - lst), maxd)
            lst = i

    ans.append(la)



for _ in range(t):
    solve()

print(*ans, sep="\n")
