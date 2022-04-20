import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, r, b = map(int, input().split())
    gap = -(-r//(b+1))
    s = gap*"R"
    r -= gap
    for i in range(b):
        s += "B"
        gap = -(-r//(b-(i)))
        s += "R" * gap
        r -= gap

    print(s)


