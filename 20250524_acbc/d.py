from functools import lru_cache

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]


@lru_cache(maxsize=None)
def dp(i, j, ans, used):
    # 終了条件：全てのマスを見終わった
    if i >= H:
        return ans
    if j >= W:
        return dp(i + 1, 0, ans, used)

    # マスの位置をビットで表現
    pos = i * W + j

    # 既に使用済みのマスの場合
    if used & (1 << pos):
        return dp(i, j + 1, ans, used)

    current_max = dp(i, j + 1, ans ^ A[i][j], used)

    # 右隣にドミノを置く
    if j + 1 < W and not (used & (1 << pos)) and not (used & (1 << (pos + 1))):
        new_used = used | (1 << pos) | (1 << (pos + 1))
        current_max = max(current_max, dp(i, j + 2, ans, new_used))

    # 下にドミノを置く
    if i + 1 < H and not (used & (1 << pos)) and not (used & (1 << (pos + W))):
        new_used = used | (1 << pos) | (1 << (pos + W))
        current_max = max(current_max, dp(i, j + 1, ans, new_used))

    # ドミノを置かない
    current_max = max(current_max, dp(i, j + 1, ans ^ A[i][j], used))

    return current_max


result = dp(0, 0, 0, 0)
print(result)
