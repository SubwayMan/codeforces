n = int(input())
for _ in range(n):
    c = input()
    k = min(c, key=ord)
    c = [*c]
    c[c.index(k)] = ""
    print(k, "".join(c))
