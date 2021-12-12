import sys
input = sys.stdin.readline

def isprime(k):
    if k==2:
        return True
    if k < 2 or k%2==0:
        return False

    for i in range(3, int(k**0.5)+1):
        if k%i==0:
            #print(k, i)
            return False
    return True

for _ in range(int(input())):
    n, e = map(int, input().split())
    a = [*map(int, input().split())]
    ans = 0

    i = 0
    while i < n:
        if isprime(a[i]):
            #print(a[i])
            x = 0
            y = 0
            for pos in range(i+e, n, e):
                if a[pos] != 1:
                    break
                x += 1
            
            for pos in range(i-e, -1, -e):
                if a[pos] != 1:
                    break
                y += 1
            #print("p", a[i], x, y)
            ans += x + y + x*y
        i += 1
    print(ans)
