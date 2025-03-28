H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

print(S)

ans = 0
# すでに訪れたマスを記録する配列
visited = [[False] * W for _ in range(H)]
print(visited)


# k 回移動してマス (i, j) にいる状態から探索を開始する
def rec(i, j, k):
    global ans
    if k == K:
        # K 回移動することができたら，答えに 1 を足して探索を終了
        ans += 1
        return
    # (i, j) を訪問済として記録する
    visited[i][j] = True
    # 隣接する 4 マスへの移動を試す
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i + di, j + dj
        # 移動先がマス目の中にあり，空きマスであり，まだ訪れていないならば，そこへ移動し再帰的に探索する
        if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == "." and not visited[ni][nj]:
            rec(ni, nj, k + 1)
    # (i, j) を訪れなかったことにする
    visited[i][j] = False


# (i0, j0) をすべて試す
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            rec(i, j, 0)
print(ans)
