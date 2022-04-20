import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))

    h = set(c)
    ans = len(h)

    for i in h:
        if c.count(i) > 1 and i != 0 and ((i * -1) not in h):
            ans += 1

    print(ans)
