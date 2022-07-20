import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input().rstrip()
    a = 0
    if s.endswith("A"):
        print("No")
        continue
    for ch in s:
        if ch == "A":
            a += 1
        elif ch == "B":
            a -= 1
        if a < 0:
            print("NO")
            break
    else:
        print("YES")
