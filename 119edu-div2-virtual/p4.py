import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(set(a))
    
    for i in range(len(b)):
        max3 = max(b[i]//3-1, 0)
        b[i] -= 3*max3

    b = sorted(set(b)) 
    y = [0 for i in range(6)]
    for i in b:
        if i <= 3:
            y[i] = 1
        if i >= 6:

