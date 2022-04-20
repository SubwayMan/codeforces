import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input()[:-1]
    a = s.count("0")
    b = len(s) - a
    if a == b:
        print(a-1)
    else:
        print(min(a, b))

