import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    fr = [0 for i in range(n+1)]
    for i in a:
        fr[i] += 1
    
    if fr[0] == 0:
        print(*([0] + [-1 for i in range(n)]))
        continue
    else:
        ans = [fr[0]]
        st = [0 for i in range(fr[0]-1)]
    
    work = 0
    for i in range(1, n+1):
        ans.append(fr[i] + work)
        
        if fr[i] == 0:
            if not st:
                ans += [-1] * (n-i)
                break
                
            pot = st.pop(-1)
            fr[i] = 1
            work += (i-pot)

        else:
            for j in range(fr[i]-1):
                st.append(i)



    print(*ans)


