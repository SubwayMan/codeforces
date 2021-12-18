
import sys
input = sys.stdin.readline 

def tri(k):
    return int((k+1)*(k/2))

def solve():
    n = int(input())
    b = list(map(int, input().split()))
    ans = []
    fsum = tri(n)
    bsum = sum(b)
    if bsum % fsum:
        print("nO")
        return
    fsum = bsum//fsum

    for i in range(n):
        diff = b[(i-1)%n] - b[i]
        diff += fsum
        if diff % n or diff <= 0:
            print("No")
            return
        ans.append(diff//n)
    print("YeS")
    print(*ans)

        


for _ in range(int(input())):
    solve()
