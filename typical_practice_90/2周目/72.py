H, W = map(int, input().split())

G = [list(input()) for _ in range(H)]

visited = [[False] * W for _ in range(H)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def isValid(r, c):
    return 0 <= r < H and 0 <= c < W and G[r][c] != "#"


ans = -1
for sr in range(H):
    for sc in range(W):
        if G[sr][sc] == "#":
            continue

        dist = [[-1] * W for _ in range(H)]
        dist[sr][sc] = 0

        def dfs(r, c):
            best = -1
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not isValid(nr, nc):
                    continue

                if nr == sr and nc == sc:
                    cycle_len = dist[r][c] + 1
                    if cycle_len >= 3:
                        best = max(best, cycle_len)
                    continue

                if dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    best = max(best, dfs(nr, nc))
                    dist[nr][nc] = -1  # バックトラック
            return best

        ans = max(ans, dfs(sr, sc))
print(ans)
