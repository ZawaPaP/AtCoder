H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0

visited = [[False] * W for _ in range(H)]


def rec(i, j, k):
    global ans

    if k == K:
        ans += 1
        return

    # 訪問済みにする
    visited[i][j] = True

    # 上下左右の４マスへの移動
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj

        if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "." and not visited[ni][nj]:
            rec(ni, nj, k + 1)

    visited[i][j] = False


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            rec(i, j, 0)

print(ans)
