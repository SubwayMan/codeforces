n = int(input())

for i in range(n):
    c = int(input())
    m = [*map(int, input().split())]
    ans = 0
    for q in range(c):
        ans = max(ans, m[q] - (q+1)) 

    print(ans)
