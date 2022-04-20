import sys
input = sys.stdin.readline

t = int(input())
ceil = lambda a, b: -(-a//b)

for _ in range(t):
    hc, dc = map(int, input().split())
    hm, dm = map(int, input().split())
    
    k, w, a = map(int, input().split())
    hc += k*a
    for i in range(k+1):
        if ceil(hm, dc) <= ceil(hc, dm):
            print("yEs")
            break
        hc -= a
        dc += w
    else:
        print("nO")
        


