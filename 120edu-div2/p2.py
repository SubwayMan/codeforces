import sys
input = sys.stdin.readline

def solve(n, p, s):
    upv = set()
    dv = set()
    n1 = []
    n2 = []
    for i in range(len(p)):
        if s[i] == "1":
            upv.add(p[i])
            n2.append((p[i], i))
        else:
            dv.add(p[i])
            n1.append((p[i], i))
    n1.sort()
    n2.sort()
    dv = sorted(range(1, len(dv)+1))
    upv = sorted(range(len(dv)+1, len(p)+1))
    
    for comp, voted in zip([n1, n2], [sorted(dv), sorted(upv)]):
        for i in range(len(comp)):
            elem, ind = comp[i]
            p[ind] = voted[i]
    print(*p)

for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    s = input().rstrip()
    solve(n, p, s)

    

    

