import sys
input = sys.stdin.readline

def bits_set(bit, x, y):
    modval = 2**bit
    x0 = x - (x%(modval))
    y0 = y - (y%(modval))
    ans = (y0-x0)//(modval*2)


for _ in range(int(input())):
    l, r = map(int, input().split())
    d = [2**k for k in range(20)]

    c = 0
    for i in d:
        if l<=i<=r:
            c += 1
    print(c)
