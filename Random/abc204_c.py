from collections import deque

N, M = map(int, input().split())

roads = {}

for _ in range(M):
    a, b = map(int, input().split())

    roads.setdefault(a, []).append(b)


def bfs(start, roads, N, ans):
    visited = [False] * (N + 1)
    visited[start] = True
    ans.add((start, start))

    Q = deque()
    Q.append(start)

    while Q:
        current = Q.popleft()
        if current in roads:
            for next in roads[current]:
                if not visited[next]:
                    visited[next] = True
                    ans.add((start, next))
                    Q.append(next)


ans = set()

for start in range(1, N + 1):
    bfs(start, roads, N, ans)

print(len(ans))
