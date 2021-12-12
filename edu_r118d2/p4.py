import sys
input = sys.stdin.readline

t = int(input())
inf = 998244353 

def phi(i, mex, lock):
    if i==n:
        return 1

    if dp[i][mex][int(lock)] != -1:
        return dp[i][mex][int(lock)]

    if lock:
        if abs(a[i] - mex) == 1:
            dp[i][mex][int(lock)] = ((phi(i+1, mex, True) % inf)*2) % inf

        else:
            dp[i][mex][int(lock)] = phi(i+1, mex, True) % inf
    else:
        if a[i] - mex == 1:
            dp[i][mex][int(lock)] = (phi(i+1, mex, False) % inf + phi(i+1, mex, True) % inf) % inf

        elif a[i] - mex == -1:
            dp[i][mex][int(lock)] = (phi(i+1, mex, False) * 2) % inf

        elif a[i] == mex:
            dp[i][mex][int(lock)] = (phi(i+1, mex, False) + phi(i+1, mex+1, False)) % inf

        else:
            dp[i][mex][int(lock)] = (phi(i+1, mex, False)) % inf
    
    return dp[i][mex][int(lock)]

for _ in range(t):
    n = int(input())
    a = [*map(int, input().split())]
    dp = [[[-1 for i in range(2)] for j in range(n+1)] for k in range(n+1)]

    print(phi(0, 0, False)-1)
    print("l", len(dp))
    for rr in dp:
        print(*rr, sep="\n", end="\n\n")

    
