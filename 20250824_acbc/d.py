from collections import deque


H, W = map(int, input().split())

Grid = [list(input()) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if Grid[i][j] == "S":
            s_r = i
            s_c = j
        if Grid[i][j] == "G":
            g_r = i
            g_c = j

even_min_operation_counts = [[float("inf")] * W for _ in range(H)]
odd_min_operation_counts = [[float("inf")] * W for _ in range(H)]
even_min_operation_counts[s_r][s_c] = 0

switch_even_visited = [[False] * W for _ in range(H)]
switch_odd_visited = [[False] * W for _ in range(H)]
switch_even_visited[s_r][s_c] = True

stack = deque()
stack.append((s_r, s_c, 0, 0))

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while stack:
    current_r, current_c, switch_count, operation_count = stack.popleft()
    for direction in DIRS:
        next_r = current_r + direction[0]
        next_c = current_c + direction[1]

        if (
            (not (0 <= next_r < H and 0 <= next_c < W))
            or Grid[next_r][next_c] == "#"
            or (switch_count % 2 == 0 and Grid[next_r][next_c] == "x")
            or (switch_count % 2 == 1 and Grid[next_r][next_c] == "o")
        ):
            continue

        if switch_count % 2 == 0:
            if switch_even_visited[next_r][next_c]:
                continue
            switch_even_visited[next_r][next_c] = True
        else:
            if switch_odd_visited[next_r][next_c]:
                continue
            switch_odd_visited[next_r][next_c] = True

        if switch_count % 2 == 0:
            even_min_operation_counts[next_r][next_c] = min(
                even_min_operation_counts[next_r][next_c], operation_count + 1
            )
        else:
            odd_min_operation_counts[next_r][next_c] = min(
                odd_min_operation_counts[next_r][next_c], operation_count + 1
            )
        if Grid[next_r][next_c] == "?":
            stack.append((next_r, next_c, switch_count + 1, operation_count + 1))
        else:
            stack.append((next_r, next_c, switch_count, operation_count + 1))

ans = min(
    even_min_operation_counts[g_r][g_c],
    odd_min_operation_counts[g_r][g_c],
)
print(ans if ans != float("inf") else -1)
