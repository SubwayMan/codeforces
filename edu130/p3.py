import sys
input = sys.stdin.readline

t = int(input())

def solve():
    n = int(input())
    s1 = input().rstrip()
    s2 = input().rstrip()
    
    for z in "abc":
        if s1.count(z)!=s2.count(z):
            print("nO")
            return

    bs1 = "".join([i for i in s1 if i != "b"])
    bs2 = "".join([i for i in s2 if i != "b"])

    if bs1!=bs2:
        print("NO")
        return

    b1 = 0
    b2 = 0
    i2 = 0

    for i in range(n):

        if s1[i] == "c":
            while s2[i2] != "c":
                i2 += 1
                b2 += 1
            if b1 < b2:
                print("NO")
                return
            i2 += 1

        if s1[i] == "a":
            while s2[i2] != "a":
                i2 += 1
                b2 += 1

            if b1>b2:
                print("NO")
                return
            i2 += 1

        if s1[i]=="b": b1+=1

    print("YES")

        

for i in range(t):
    solve()

