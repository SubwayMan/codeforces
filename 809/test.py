def allp(n):
    ans = set()
    for i in range(1, n+2):
        ans.add(n//i)
    return ans

def allp2(n):
    ans = set()
    ans.add(0)
    for i in range(1, int(n**0.5)+1):
        ans.add(n//i)
        ans.add(n//(n//i))
    return ans

for i in range(3000):
    if allp(i) != allp2(i):
        print(i, allp(i), allp2(i))
