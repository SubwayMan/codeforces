import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    st = input()[:-1]
    k = st[0]
    hold = ""

    if n >= 2 and st[0] == st[1]:
        print(st[:2])
        continue

    for i in range(1, n):
        if ord(st[i]) < ord(st[i-1]):
            k += hold + st[i]
        elif ord(st[i]) == ord(st[i-1]):
            hold += st[i]
        else:
            break
    print(k + k[::-1])
