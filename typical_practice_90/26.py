from collections import deque

N = int(input())

G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

# 2彩色（二部グラフ）の構築
color = [-1] * (N + 1)
color[1] = 0  # 始点を色0に
queue = deque([1])

while queue:
    current = queue.popleft()
    for node in G[current]:
        if color[node] == -1:
            # currentと別の色で塗り分け (0 or 1)
            color[node] = 1 - color[current]
            queue.append(node)

# 色0と色1の頂点を集める
vertices_color0 = [node for node in range(1, N + 1) if color[node] == 0]
vertices_color1 = [node for node in range(1, N + 1) if color[node] == 1]

# より多い方を選ぶ
if len(vertices_color0) >= len(vertices_color1):
    ans = vertices_color0
else:
    ans = vertices_color1

# N/2個の頂点を出力
print(*ans[: (N // 2)])
