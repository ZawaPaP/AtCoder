from collections import deque


H, W = map(int, input().split())

Grid = [list(input()) for _ in range(H)]


# turn_over_counts[i][j] は (i, j) に到達するために必要な最小の操作回数
turn_over_counts = [[float("inf")] * W for _ in range(H)]

# r, c, count, prev_mark
q = deque([(0, 0, 1 if Grid[0][0] == "#" else 0, Grid[0][0])])

DIRS = [(1, 0), (0, 1)]

while q:
    current_r, current_c, count, prev_mark = q.popleft()
    for direction in DIRS:
        next_r = current_r + direction[0]
        next_c = current_c + direction[1]

        if (
            (not (0 <= next_r < H and 0 <= next_c < W))
        ):
            continue


        if Grid[next_r][next_c] == "#" and prev_mark == ".":
            if turn_over_counts[next_r][next_c] > count + 1:
                turn_over_counts[next_r][next_c] = count + 1
            q.append((next_r, next_c, count + 1, "#"))
        elif Grid[next_r][next_c] == "." and prev_mark == "#":
            if turn_over_counts[next_r][next_c] > count:
                turn_over_counts[next_r][next_c] = count
                q.append((next_r, next_c, count, "."))
        else:
            if turn_over_counts[next_r][next_c] > count:
                turn_over_counts[next_r][next_c] = count
                q.append((next_r, next_c, count, prev_mark))
            

print(turn_over_counts[H - 1][W - 1])