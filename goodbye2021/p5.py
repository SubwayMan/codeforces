import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input()[:-1]
    t = input()[:-1]

    if "".join(sorted(s)) >= t:
        print(-1)
        continue
