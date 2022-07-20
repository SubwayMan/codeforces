import sys
input = sys.stdin.readline


def printf(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


n = int(input())
seen = []
lastpos = {}
seentot = 0
ans = ""

for i in range(1, n+1):
    printf("?", 2, 1, i)
    nc = int(input())

    if (nc > seentot):
        seentot = nc
        printf("?", 1, i)
        ch = input().rstrip()
        ans += ch
        seen.append(ch)
        lastpos[ch] = i
        continue

    for j in range(len(seen)-1, -1, -1):
        ch = seen[j]
        printf("?", 2, lastpos[ch], i)
        z1 = int(input())
        printf("?", 2, lastpos[ch], i-1)
        z2 = int(input())

        if z1 == z2:
            ans += ch
            lastpos[ch] = i
            break

printf("!", ans)


