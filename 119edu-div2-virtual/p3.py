import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k, x = map(int, input().split())
    s = input()[:-1]
    alls = True
    vals = [0]
    aval = [0]
    for ch in s:
        if ch == "a":
            alls = False
            if vals[-1] > 0:
                vals.append(0)
            aval[-1] += 1
        else:
            if aval[-1] > 0:
                aval.append(0)
            vals[-1] += 1

    if vals[-1] == 0:
        vals.pop(-1)
    if alls:
        print("b" * x)
    else:
        bval = [0 for i in range(len(vals))]
        x -= 1
        for i in range(len(vals)-1, -1, -1):
            bval[i] = (x % ((vals[i]*k)+1))
            x //= ((vals[i]) * k) + 1

        ans = ""
        if s[0] == "*":
            for i in range(len(aval)):
                ans += (bval[i]*"b") + aval[i]*"a"

        else:
            for i in range(len(bval)):
                ans +=  aval[i]*"a" + (bval[i]*"b") 

        if len(aval) > len(bval):
            ans += "a" * aval[-1]

        if len(bval) > len(aval):
            ans += "b" * bval[-1]
        print(ans)

        

