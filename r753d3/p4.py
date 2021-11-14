import sys
input = sys.stdin.readline

a = []
for _ in range(int(input())):
    n = int(input())
    k = [*map(int, input().split())]
    s = input()[:-1]

    m = ["" for i in range(n)]
    for p in zip(k, s):
        e, w = p
        m[e-1] += w

    rc = 0
    bc = 0
    for i in range(1, n+1):
        s = m[i-1]
        if not s:
            if rc: rc += 1
            else: bc += 1

        elif len(s) > 1:
            r = s.count("R")
            b = s.count("B")
            
            if b:
                if not r:
                    b -= 1
                bc += b
                rc -= b

                if rc < 0:
                    if r==1 and rc == -1:
                        bc -= 1
                        rc += 1
                    else:
                        print("NO")
                        break




