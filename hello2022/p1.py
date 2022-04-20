# virtual contest: Hello 2022
# contest 1621
# written by Tyler Chen
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    c = [["." for i in range(n)] for j in range(n)]
    if (n-1)//2 < k-1:
        print(-1)
        continue

    for i in range(0, k*2, 2):
        c[i][i] = "R"

    for r in c:
        print("".join(r))

