import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if a[-1] != b[-1]:
        print("No")
        continue

    bag = [0 for i in range(n+1)]
    b_off = 0
    for i in range(n-2, -1, -1):
        if b[i] != a[i+b_off]:
            fl = True
            if bag[a[i+b_off]]:
                bag[a[i+b_off]] -= 1
                b_off -= 1
                fl = False

            if b[i] != a[i+b_off] and b[i] == b[i+1]:
                b_off += 1
                bag[b[i]] += 1
                fl = False

            if fl:
                print("No")
                break
    else:
        print("YeS")

