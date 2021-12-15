import sys
input = sys.stdin.readline

infv = 998244353
n = int(input())
a = list(map(int, input().split()))
b = [0 for i in range(n)]
b[0] = a[0]


for i in range(1, n):
    b[i] = ((b[i-1]%infv) * ((a[i]-1)%infv))%infv
print(b[-1])

