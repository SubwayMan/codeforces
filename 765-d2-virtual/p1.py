import sys
input = sys.stdin.readline

f = []
for _ in range(int(input())):
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    k = [0 for i in range(l)]
    for i in range(l):
        for x in a:
            if (1<<i)&x:
                k[i] += 1
    st = ""
    for i in k:
        if i > (n//2):
            st = "1" + st
        else:
            st = "0" + st
    f.append(int(st, 2))

print(*f, sep="\n")
