import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, h = map(int, input().split())

    a = [*map(int, input().split())]
    a.sort(reverse=True)
    a1, a2 = a[0], a[1]
    
    c = (-(-h//(a1+a2)))*2
    if (c//2)*(a1+a2)-a2>=h:c-=1
    print(c)
