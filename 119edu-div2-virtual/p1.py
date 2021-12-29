import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input()[:-1]
    if s.count("N") == 1:
        print("nO")
    else:
        print("YeS")
