import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = float('inf')
for i in range(n):
    lans = 0
    val = 1
    for dec in range(i-1, -1, -1):
        c = -(-val//a[dec])
        lans += c
        val = c * a[dec] + 1

    
    val = 1
    for inc in range(i+1, n):
        c = -(-val//a[inc])
        lans += c
        val = c * a[inc] + 1
    ans = min(ans, lans)

print(ans)

