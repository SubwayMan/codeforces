import sys
input = sys.stdin.readline

#t = int(input())
t = 1

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    pre = [0]

    for i in range(n):
        pre.append(pre[-1]+a[i])
    
    for i in range(q):
        x, y = map(int, input().split())
        print(pre[x] - pre[x-y])


    


for i in range(t):
    solve()
