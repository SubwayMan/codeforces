import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = input()[:-1]
    if len(s)%2:
        print("nO")
    else:
        if s[:len(s)//2] == s[len(s)//2:]:
            print("yes")
        else:
            print("no")
