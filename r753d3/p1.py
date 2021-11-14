import sys
input = sys.stdin.readline

for _ in range(int(input())):
    alp = input()[:-1]
    c = 0
    k = input()[:-1]
    for i in range(1, len(k)):
        c+=abs(alp.find(k[i])-alp.find(k[i-1]))

    print(c)
