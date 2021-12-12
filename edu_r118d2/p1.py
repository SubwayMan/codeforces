import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    a, b = map(int, input().split())
    k = len(str(a))-1

    if a >= 10:
        a /= (10**k)
    k += b

    a2, b = map(int, input().split())
    k2 = len(str(a2))-1

    if a2 >= 10:
        a2 /= (10**k2)
    k2 += b


    if (k, a) > (k2, a2):
        print(">")
    elif (k, a) < (k2, a2):
        print("<")
    else:
        print("=")
