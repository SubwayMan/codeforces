# virtual contest: Hello 2022
# contest 1621
# written by Tyler Chen
import sys
input = sys.stdin.readline


def iprint(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


t = int(input())

for _ in range(t):
    ind = 1
    n = int(input())

    perm = [0 for i in range(n)]
    cycle = []

    while ind <= n:
        if perm[ind-1]:
            ind += 1
            continue

        iprint("?", ind)
        comm = int(input())
        cycle.append(comm)
        if len(cycle) > 1 and comm == cycle[0]:
            perm[ind-1] = cycle[0]
            for i in range(1, len(cycle)):
                perm[cycle[i-1]-1] = cycle[i]
            ind += 1
            cycle = []
    iprint("!", *perm)
