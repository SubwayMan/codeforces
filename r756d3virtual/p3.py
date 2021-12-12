import sys
from collections import deque
input = sys.stdin.readline

ans = []
t = int(input())
for _ in range(t):
    n = int(input())
    a = deque([*map(int, input().split())])
    
    ans = deque()
    if n not in (a[0], a[-1]):
        print(-1)
        continue
    
    if a[0] == n:
        ans.append(a.popleft())
    else:
        ans.append(a.pop())

    while a:

        if a[0] > a[-1]:
            ans.appendleft(a.popleft())
        else:
            ans.append(a.pop())

    print(*ans)


