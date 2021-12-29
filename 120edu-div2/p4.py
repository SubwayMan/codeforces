import sys
from collections import deque
from math import factorial as fact

input = sys.stdin.readline

mod = 998244353

n, k = map(int, input().split())
st = input().rstrip()
tot1 = 0
ans = 0
ipos = deque([-1])

for i in range(n):
    if st[i] == "1":
        ipos.append(i)
        if tot1 == k:
            try:
                ans -= lpos - 1
            except:
                pass
            lpos = ipos.popleft()
            lpos = i - lpos
            ans += fact(lpos)//(fact(k) * fact(lpos-k))
            tot1 -= 1
        tot1 += 1

print(ans)


