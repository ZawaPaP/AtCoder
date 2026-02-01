from collections import deque

H, W = map(int, input().split())
sr, sc = map(int, input().split())
gr, gc = map(int, input().split())


S = [list(input()) for _ in range(H)]

# 距離（曲がり回数）のみを管理。初期値は無限大
dist = [[float("inf")] * W for _ in range(H)]

q = deque([(sr - 1, sc - 1)])
dist[sr - 1][sc - 1] = 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while q:
    r, c = q.popleft()

    if r == gr - 1 and c == gc - 1:
        break

    cur_dist = dist[r][c]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        while 0 <= nr < H and 0 <= nc < W and S[nr][nc] == ".":
            # 短い手数で到達済みなら計算不要
            if dist[nr][nc] <= cur_dist:
                break

            # 短い手数が見つかったら、qに追加して探索
            if dist[nr][nc] > cur_dist + 1:
                dist[nr][nc] = cur_dist + 1
                q.append((nr, nc))

            # 同じ手数ならqに入れない
            nr += dr
            nc += dc
print(dist[gr - 1][gc - 1] - 1)
