import sys
input = sys.stdin.readline

t = 1
t = int(input())
alla = []

def nch(ch):
    return ord(ch) - ord('a')

def solve():
    p = input().rstrip()
    ans = (nch(p[0])*26 + nch(p[1])) + 1
    nans = ans
    for i in range(0, 1000, 27):
        if i < ans:
            nans -= 1
    alla.append(nans)



for _ in range(t):
    solve()

print(*alla, sep="\n")
