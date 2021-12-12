import sys
input = sys.stdin.readline

n, q = map(int, input().split())
s = input()[:-1]

c = 0
i = 0
indx = [0 for i in range(n)]

while i < n-2:
    if s[i:i+3] == "abc":
        c += 1
        indx[i] = 1
        i += 2
    i += 1

p = list(s)
for _ in range(q):
    i, e = input().split()
    i = int(i) - 1

    if p[i] == e:
        print(c)
        continue

    p[i] = e

    i0 = max(0, i-2)
    for y in range(i0, i+1):
        if indx[y]:
            indx[y] = 0
            c -= 1
        else:
            if y+2 >= n:
                continue
            if p[y:y+3] == ["a","b","c"]:
                indx[y] =1
                c += 1

    #print(p)
    #print(indx)
    print(c)
        



        
    
