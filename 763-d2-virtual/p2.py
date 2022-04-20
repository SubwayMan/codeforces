import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    k = []

    for i in range(n):
        k.append(tuple(map(int, input().split())))

    k.sort(key = lambda a: abs(a[0] - a[1]))

    ans = [0 for i in range(n)]
    seen = set()
    coords = set(range(n))

    while coords:
        nc = coords.copy()
        for i in coords:
            if ans[i]:
                continue

            p1, p2 = k[i]
            if p1 == p2:
                ans[i] = p1
                seen.add(p1)
                nc.remove(i)
            else:
                p = 0
                repl = 0
                for x in range(p1, p2+1):
                    if x not in seen:
                        repl = x
                        p += 1

                if p == 1:
                    ans[i] = repl
                    seen.add(repl)
                    nc.remove(i)
        coords = nc
    
    for rang, bob in zip(k, ans):
        print(*rang, bob)
    print()



