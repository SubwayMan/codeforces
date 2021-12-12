import sys
inptu = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    print("?", 1, n)
    tot = int(input())

    lb = 1
    rb = n
    while True:
        print("?", 
