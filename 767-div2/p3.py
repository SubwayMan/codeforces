import sys
input = sys.stdin.readline


def maxmex(p1, mex):

    d = set(range(mex))
    nmex = mex

    for i in range(p1, n):
        d -= {a[i], }
        ch_arr[a[i]] -= 1
        if ch_arr[a[i]] == 0 and a[i] < nmex:
            nmex = a[i]
            
        if not d:
            return (mex, i+1, nmex)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    ch_arr = [0 for i in range(n + 1)]
    for x in a:
        ch_arr[x] += 1
    for i in range(n+2):
        if ch_arr[i] == 0:
            mex = i
            break

    af = 0
    while af != n:
        x, na, nx = maxmex(af, mex)
        ans.append(x)
        af = na
        mex = nx

    print(len(ans))
    print(*ans)

