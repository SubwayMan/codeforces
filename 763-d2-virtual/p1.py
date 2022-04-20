import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, ri, ci, rf, cf = map(int, input().split())

    ans = float('inf')
    if ri <= rf:
        ans = min(ans, rf - ri)
    else:
        ans = min(ans, (n - ri) + (n - rf))

    if ci <= cf:
        ans = min(ans, cf - ci)
    else:
        ans = min(ans, (m - ci) + (m - cf))

    print(ans)


   
