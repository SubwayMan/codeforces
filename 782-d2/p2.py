import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    zk = k
    s = int(input(), 2)
    a = [0 for i in range(n)]
    ans = ""

    for i in range(n-1, -1, -1):
        if k:
            if i == 0:
                if (k & 1):
                    s ^= 1

                a[n-1] = k
                break

            if bool((1<<i) & s) == zk%2:
                s ^= (1<<i)
                k -= 1
                a[n-1-i] = 1
        else:
            break

    if zk % 2:
        s ^= 2**n - 1
        
    print(bin(s)[2:].rjust(n, "0"))
    print(*a)
        
