from collections import deque


H, W = map(int, input().split())

N = int(input())

A = list(map(int, input().split()))

Grid = [[0] * W for _ in range(H)]

color_q = deque()
for i, a in enumerate(A):
    color_q.append((i + 1, a))

# 左上から右下に向かって 連結するように Grid[i][j] に色を塗る

down = (1, 0)
right = (0, 1)
up = (-1, 0)

q = deque()
q.append((0, 0, 'down'))
while color_q:
    color, count = color_q.popleft()
    while q and count > 0:
        r, c, prev_direction = q.popleft()
        if not (0 <= r < H and 0 <= c < W) or Grid[r][c] != 0:
            continue
        Grid[r][c] = color
        count -= 1
        if prev_direction != 'up' and r < H - 1:
            q.append((r + down[0], c + down[1], 'down'))
        elif prev_direction != 'down' and r != 0:
            q.append((r + up[0], c + up[1], 'up'))
        else:
            q.append((r + right[0], c + right[1], 'right'))


for row in Grid:
    print(*row)
