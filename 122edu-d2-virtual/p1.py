import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    diff = n%7
    last = n%10
    if n%7 == 0:
        pass
    elif (7-diff)+last >= 10:
        n -= diff
    else:
        n += (7 - diff)
    print(n)
