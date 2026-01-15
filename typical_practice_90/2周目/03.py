from collections import deque

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)


# 求める長さは、木の直径
# 木の直径は BFS2回で解く
# 1回目で最長となる点を端点とし、2回目のBFSで端点からの最長距離を出す

def get_longest_path(n):
    Q = deque()
    dist = [-1 for _ in range(N)]

    Q.append(n)
    dist[n] = 0

    while Q:
        curr = Q.pop()
        for nxt in G[curr]:
            # 一度訪れていた場合はNG
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[curr] + 1
            Q.append(nxt)
    return dist.index(max(dist)), max(dist)


edge, l = get_longest_path(0)
edge_node, longest = get_longest_path(edge)
print(longest + 1)
