a, b = map(int, input().split())
a = bin(a)[2:]
b = bin(b)[2:]

def transit(s1, s2):
    a1 = s1.split("0")
    a2 = s2.split("0")
    sl1, sr1 = a1[0], a1[-1]
    sl2, sr2 = a2[0], a2[-1]

    if len(sl1) <= len(sl2) and len(sr1) <= len(sr2):
        if s1.strip("1") == s2.strip("1"):
            return True
    return False
    
    
if a == b:
    print("yEs")
else:
    k = [a.rstrip("0"), a + "1"]
    for i in k.copy():
        k.append(i[::-1])

    for el in k:
        if transit(el, b):
            print("YEs")
            break
    else:
        print("no")
