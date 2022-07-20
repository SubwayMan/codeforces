import sys
input = sys.stdin.readline

t = 1
t = int(input())

tris = [0]
ln = [0, 0, 0]
p = 0
tr = 0

while tr < 10**9:
    tr += 2 * (sum(ln) - ln[p])
    ln[p] += 1
    p = (p+1) % 3
    tris.append(tr)

def solve():
    n = int(input())
    ans = 0
    jump = 2**16
    ov = len(tris)
    while jump:
        while (ans+jump < ov and tris[ans+jump] < n):
            ans += jump
        jump //= 2
    print(ans+1)



for _ in range(t):
    solve()
