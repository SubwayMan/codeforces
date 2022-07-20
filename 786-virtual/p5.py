import sys
input = sys.stdin.readline

t = 1
inf = 10**11

def cl(n, x):
    return -(-n//x)

def m_adj(a, b):
    if a>b:
        a, b = b, a
    ans = cl(b, 2)
    if ans >= a: return ans
    na = b-a
    a -= ans
    ans += cl(a, 2)
    b -= na*2
    oans = (b//3) * 2
    if b%3 == 1:
        oans += 1
    elif b%3 == 2:
        oans += 2
    return min(ans, na+oans)


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = inf
    a.insert(0, inf)
    a.append(inf)
    for i in range(1, n+1):
        el, er = (a[i-1], a[i+1])
        lans = min(el, er) + cl(abs(el-er), 2)
        lans = min(lans, max(el, er))
        lans = min((lans, m_adj(a[i-1], a[i]), m_adj(a[i], a[i+1])))
        ans = min(ans, lans)
    a.sort()
    ans = min(ans, cl(a[0], 2) + cl(a[1], 2))
    print(ans)

for _ in range(t):
    solve()
