import sys
input = sys.stdin.readline
import math
t = int(input())

for _ in range(t):
    l = int(input())
    a = [*map(int, input().split())]
    bts = set()
    for b in range(30):
        c = 0
        for ai in a:
            if (1<<b)&ai:
                c+=1
        bts.add(c)
    gf = bts.pop()
    for v in bts:
        gf = math.gcd(gf, v)
    if gf == 0:
        print(*range(1, len(a)+1))
    else:
        ans = []
        for f in range(1, int(math.sqrt(gf))+1):
            if not gf%f:
                if int(math.sqrt(gf))==math.sqrt(gf)==f:
                    ans.append(int(math.sqrt(gf)))
                else: ans.extend([f, gf//f])

        ans.sort()
        print(*ans)





