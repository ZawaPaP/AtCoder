from collections import deque

H, W = map(int, input().split())

# 最短距離を保存する配列
distance = [[float("inf") for _ in range(W)] for _ in range(H)]

# 出口を記録する
exits = []

grids = []

for i in range(H):
    S = list(input())
    for j, c in enumerate(S):
        if c == "E":
            exits.append((i, j))
            distance[i][j] = 0
    grids.append(S)


def update_distance(grids, distance, exits):
    # 方向定義（定数化して繰り返し計算を避ける）
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    H, W = len(grids), len(grids[0])

    # 全ての出口から同時にBFSを開始
    Q = deque(exits)

    while Q:
        r, c = Q.popleft()
        curr_dist = distance[r][c]

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if (
                0 <= nr < H
                and 0 <= nc < W
                and grids[nr][nc] != "#"  # 壁以外のマスを全て探索
            ):
                # 新しい距離を計算
                new_dist = curr_dist + 1

                # 距離が実際に更新される場合のみキューに追加
                if new_dist < distance[nr][nc]:
                    distance[nr][nc] = new_dist
                    Q.append((nr, nc))


# 一度のBFSで全ての出口からの距離を計算
update_distance(grids, distance, exits)

# 各マスから出口までの最短距離に合わせて、矢印を配置
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dir_chars = ["v", ">", "^", "<"]

for i in range(H):
    for j in range(W):
        # 通行可能なマス（壁でないマス）のみ考慮
        if grids[i][j] != ".":
            continue

        min_dist = float("inf")
        best_dir = -1

        # 最も距離の短い方向を探す
        for k, (dr, dc) in enumerate(dirs):
            nr, nc = i + dr, j + dc

            if (
                0 <= nr < H
                and 0 <= nc < W
                and distance[nr][nc] != float("inf")
                and distance[i][j] > distance[nr][nc]
                and distance[nr][nc] < min_dist
            ):
                min_dist = distance[nr][nc]
                best_dir = k

        # 最も近い出口への方向がある場合、矢印を配置
        if best_dir != -1:
            grids[i][j] = dir_chars[best_dir]

for i in grids:
    print("".join(i))
