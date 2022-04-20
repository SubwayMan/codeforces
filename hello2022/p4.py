# virtual contest: Hello 2022
# contest 1621
# written by Tyler Chen
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    mt = []
    for i in range(n*2):
        mt.append(list(map(int, input().split())))

    ans = 0
    for r in range(n, n*2):
        for c in range(n, n*2):
            ans += mt[r][c]

    addf = min(mt[0][2*n-1], mt[2*n-1][0], mt[n-1][2*n-1], mt[2*n-1][n-1], mt[n][n-1], mt[n-1][n], mt[0][n], mt[n][0])
    ans += addf
    print(ans)
