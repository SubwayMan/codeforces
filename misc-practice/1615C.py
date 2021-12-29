import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    s = input()[:-1]
    s2 = input()[:-1]
    
    pos1 = [0, 0]
    pos2 = [0, 0]
    comp = int(s2, 2)

    for i in range(len(s)):
        if s[i] != s2[i]:
            pos1[int(s[i])] += 1
        else:
            pos2[int(s[i])] += 1
    ans = []

    if pos1[0] == pos1[1]:
        ans.append(sum(pos1))

    if pos2[1] == pos2[0]+1:
        ans.append(sum(pos2))

    if ans:
        print(min(ans))
    else:
        print(-1)

