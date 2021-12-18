import sys
input = sys.stdin.readline 

for _ in range(int(input())):
    n = int(input())
    bi = input()[:-1].split()
    s = bi[0][0]
    for i in range(1, n-2):
        y = bi[i]
        if y[0] != bi[i-1][1]:
            s += bi[i-1][1]
        s += y[0]

    s += bi[-1][1]
    s += (n - len(s)) * "a"
    print(s)

