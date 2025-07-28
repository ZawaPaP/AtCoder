N, M = map(int, input().split())

Moves = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    Moves[a].append([b, c])
    Moves[b].append([a, c])

K, T = map(int, input().split())

D = list(map(int, input().split()))

for i in range(len(D) - 1):
    Moves[D[i]].append([D[i + 1], T])
    Moves[D[i + 1]].append([D[i], T])

Q = int(input())

INF = float("inf")


for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        x, y, t = q[1], q[2], q[3]
        Moves[x].append([y, t])
        Moves[y].append([x, t])
    elif q[0] == 2:
        x = q[1]
        if x in D:
            continue
        for i in range(len(D)):
            Moves[D[i]].append([x, T])
            Moves[x].append([D[i], T])
        D.append(x)
    else:
        pass
