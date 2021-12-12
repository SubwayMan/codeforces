
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    a1 = sorted(a)
    b.sort()
    print(a1)
    print(b)

    l = 0
    p = {}
    for i in range(n):
        if a1[i] != b[i]:
            l += 1
            if b[i] not in p.keys():
                p[b[i]] = 0
            p[b[i]] += 1
    print(l)
    print(p)
    for i in range(n-(l-1)):
        v = a[i:i+l]
        print(v)
        for j in p:
            if v.count(j-1) != p[j]:
                break
        else:
            print("yEs")
            break
    else:
        print("No")



