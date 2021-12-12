import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = input()[:-1]
p = list(s)

la = n+2
ra = 0
lb = n+1
rb = 0
lc = n+3
rc = 0

for i in range(1, n+1):
    if s[i-1] == "a":
        la = min(la, i)
    elif s[i-1] == "b":
        lb = min(lb, i)
        rb = max(rb, i)
    else:
        lc = min(lc, i)
        rc = max(rc, i)

vals = [s[la-1:ra].count("a"), s[lb-1:rb].count("b"), s[lc-1:rc].count("c")]


for _ in range(q):
    i, c = input().split()
    i = int(i)
    if p[i-1] == c:
        print(min(vals))
        continue
    

        


