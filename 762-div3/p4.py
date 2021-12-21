import sys
input = sys.stdin.readline

for _ in range(int(input())):
    input()
    m, n = map(int, input().split())
    joys = [0 for i in range(n)]
    shops = []
    for i in range(m):
        shops.append(tuple(map(int, input().split())))

    taken = set()
    for i in range(n-1):
        cum = joys.copy()
        hold = None
        for shop in shops:
            if shop not in taken:
                pot = list(map(sum, zip(joys, shop)))

                if min(pot) > min(cum):
                    cum = pot
                    hold = shop

        if hold:
            joys = cum
            taken.add(hold)

    print(min(joys))





