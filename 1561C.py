n = int(input())
aw=[]
for _ in range(n):
    i = int(input())
    h = []
    for po in range(i):
        zh, *k = map(int, input().split())
        c = 0
        p = 0
        for ki in k:
            if c<=ki:
                p += (ki+1)-c
                c = ki + 1
            c += 1
        h.append((p, c, zh))

    h.sort(key=lambda a: a[0])
    ans = 0
    hold = 0
    for pa in h:
        pi, pf, le = pa
        if pi>hold:
            ans += (pi)-hold
        hold = max(hold+le, pf)

    aw.append(ans)
    #print(*h, sep="\n")
print(*aw, sep="\n")

