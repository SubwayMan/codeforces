import sys
input = sys.stdin.readline

for _ in range(int(input())):
    an = 0
    n, m = map(int, input().split())

    for i in range(m):
        l, r, a = map(int, input().split())
        an |= a

    print((2**(n-1)*an)%(10**9 + 7))
