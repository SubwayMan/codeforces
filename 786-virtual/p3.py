import sys
input = sys.stdin.readline

t = 1
t = int(input())

def solve():
    s = input().rstrip()
    repl = input().rstrip()
    if "a" in repl and len(repl) > 1:
        print(-1)
        return
    if repl == "a":
        print(1)
        return
    print(2**s.count("a"))


for _ in range(t):
    solve()
