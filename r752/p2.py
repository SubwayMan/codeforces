t = int(input())

for _ in range(t):
    n = int(input())
    m = [*map(int, input().split())]

    if not len(m)%2: 
        print("YES")
        continue

    for o in range(1, len(m)):
        if m[o]<=m[o-1]:
            print("YES")
            break

    else:
        print("NO")
