import sys
input = sys.stdin.readline

for _ in range(int(input())):
    l, r, k = map(int, input().split())
    if l % 2:
        u = -(-(r-l+1)//2)
    else:
        u = ((r-l+1)//2)

    if l == r:
        print(["yes", "no"][l == 1])

    else:
        print(["nO", "yEs"][u <= k])
