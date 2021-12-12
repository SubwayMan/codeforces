import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = input()[:-1]
    if any(i in "2468" for i in k):
        if k[-1] in "2468":
            print(0)
        elif k[0] in "2468":
            print(1)
        else:
            print(2)
    else:
        print(-1)
