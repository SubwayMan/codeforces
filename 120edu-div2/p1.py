import sys
input = sys.stdin.readline

def solve(a):
    for i in range(2):
        for j in range(i+1, len(a)):
            p = a.copy()
            p.remove(a[i])
            p.remove(a[j])
            if p[0] == a[i] + a[j]:
                print("YES")
                return
            if (p[0] % 2 == 0) and a[i] == a[j]:
                print("YES")
                return
    print("NO")

for _ in range(int(input())):
    a = sorted(map(int, input().split()))
    solve(a)

