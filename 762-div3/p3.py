import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, s = input()[:-1].split()
    a = a[::-1]
    s = s[::-1]
    si = 0
    i = 0
    val = ""

    while i < len(a):
        if si >= len(s):
            print(-1)
            break

        if int(a[i]) <= int(s[si]):
            val = str(int(s[si])-int(a[i])) + val
            si += 1

        else:
            v = str(int(s[si:si+2][::-1]) - int(a[i]))
            if int(v) > 9 or int(v) < 0:
                print(-1)
                break
            val = v + val
            si += 2
        i += 1
    else:
        val = s[si:][::-1] + val

        if int(val) == 0:
            print(0)
        else:
            print(val.lstrip("0"))


