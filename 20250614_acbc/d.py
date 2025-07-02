from collections import deque

N, M = map(int, input().split())

# 重みつき有向辺グラフ
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 頂点1から移動して、頂点iまでの重みのビット単位XORのあり得る値をsetに格納
xors = [set() for _ in range(N + 1)]

d = deque()
d.append(1)
while d:
    v = d.popleft()

    for u, c in graph[v]:
        if len(xors[u]) == 0 and len(xors[v]) == 0:
            xors[u].add(c)
            d.append(u)
        else:
            temp = set()
            for x in xors[v]:
                if x ^ c not in xors[u]:
                    temp.add(x ^ c)
            if len(temp) > 0:
                xors[u] = xors[u] | temp
                d.append(u)


if len(xors[N]) == 0:
    print(-1)
else:
    print(min(xors[N]))
