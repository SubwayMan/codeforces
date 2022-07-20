import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    chops = 0
    for i in a:
        chops += i-1
    if chops % 2 == 1:
        print("errorgorn")
    else:
        print("maomao90")
