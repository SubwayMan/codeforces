import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if x==y:
        print(x)
    elif x>y:
        print(x+y)
    else:
        print(y-(y%x)//2)


