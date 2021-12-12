import sys
input = sys.stdin.readline
def prime_gen(k):
    c = [False] * k
    for i in range(k):
        if not c[i]:
            yield i+2
            c[i::i+2] = [True] * len(c[i::i+2])

p = list(prime_gen(100000))
t = int(input())
for _ in range(t):
    n = int(input())
    print(*p[:n])


