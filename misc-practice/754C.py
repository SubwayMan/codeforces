import sys
input = sys.stdin.readline
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input()[:-1]
    c = s.split("a")[1:-1]
    k = 900
    for p in c:
        if p.count("b")<2 and p.count("c")<2:
            k = min(k, len(p)+2)
 
    if k==900:
        if "abbacca" in s or "accabba" in s: print(7)
        else: print(-1)
    else:print(k)
 
 
 
