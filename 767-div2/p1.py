import sys
input = sys.stdin.readline

ans = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = list(zip(a, b))
    p.sort()
    for cost, ret in p:
        if cost > k:
            break
        k += ret

    ans.append(k)

print(*ans, sep="\n")
