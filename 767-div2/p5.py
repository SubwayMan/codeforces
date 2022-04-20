import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    seen = set()
    a = [input().strip() for _ in range(n)]

    for f in a:
        seen.add(f)
        if f[::-1] in seen:
            print("yEs")
            break
    else:
        print("No")
