import sys
input = sys.stdin.readline 

for _ in range(int(input())):
    b = sorted(map(int, input().split()))
    s = b[-1]
    a1 = b[0]
    x = b[1]
    print(a1, x, s-(a1+x))
