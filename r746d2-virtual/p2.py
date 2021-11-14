import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = [*map(int, input().split())]
    fa = sorted(a)

    x, y = len(a)-x, x+1 
    if x < y:
        for i in range(x+1, y):
            if fa[i-1] != a[i-1]:
                print("nO")
                break
        else:
            print("YeS")
    else:
        print("Yes")

