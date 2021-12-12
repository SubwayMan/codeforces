import sys
input = sys.stdin.readline

t = int(input())

def pr(n, m):
    c = (n//3)*m
    d = (n%3)
    c += (-(-m//3)*d)
    return c

for _ in range(t):
    k = [*map(int, input().split())]
    n = max(k)
    m = min(k)
    print(min(pr(n, m), pr(m, n)))
