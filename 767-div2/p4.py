import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    ans = 0
    f = 0
    for i in range(n):
        row = list(map(int, input().split()))
        if i == 0 or i == n-1:
            ans ^= row[0]^row[-1]
        else:
            for j in range(1, n-1):
                ans ^= j

        for x in row:
            f ^= x
    
    ans ^= f
    print(ans)
