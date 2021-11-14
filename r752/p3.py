import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    m = [*map(int, input().split())]
    
    k =[]
    fl = False
    for i in range(len(m)):
        c = 0
        for j in range(i+2, 1, -1):
            if m[i]%j:
                k.append(c)
                break
            c+=1
        else:
            k.append(-1)
            fl = True
            break

    if fl:
        print("NO")
        continue

    for j in range(n):
        if k[j] > j:
            print("NO")
            break
    else:
        print("YES")
