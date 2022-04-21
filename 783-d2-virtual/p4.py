import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.append(-float('inf'))
    ans = 1
    segs = []
    h = -1
    seg = 0
    pref = [0] * (n+1)
    for i in range(1, n+1):
        pref[i] = pref[i-1] + a[i-1]

    seen = [0 for i in range(n+1)]
    seen[-1] = 1
    for i in range(n+1):
        if a[i] > 0:
            ans += 1
            if h == -1:
                h = i
            seg += 1
        elif a[i] < 0:
            ans -= 1
            if h != -1:
                segs.append((i-seg, i-1, pref[i] - pref[i-seg]))
                seen[i-seg] = 1
                seen[i-1] = 1
                h = -1
            seg = 0
        else:
            seg += 1
    
    for l, r, tot in segs:
        lind = l-1
        rind = r+1
        while True:
            tans = []
            if a[lind] + tot > 0 and not seen[lind]:
                tans.append((a[lind], 0)) 

            if a[rind] + tot > 0 and not seen[rind]:
                tans.append((a[rind], 1))

            if not tans:
                break

            val, ni = max(tans)
            if ni:
                seen[rind] = 1
                tot += a[rind]
                rind += 1
                if a[rind] == 0: 
                    ans -= 1
                ans += 2
            else:
                if a[lind] == 0: 
                    ans -= 1
                seen[lind] = 1
                tot += a[lind]
                lind -= 1
                ans += 2
    print(ans)


