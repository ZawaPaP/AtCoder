from collections import defaultdict

H, W = map(int, input().split())

P = [list(map(int, input().split())) for _ in range(H)]

ans = 1
# bit全探索
for mask in range(1, 1 << H):
    # maskのbitが立っている行だけを選ぶ
    target_h = [i for i in range(H) if mask & (1 << i)]

    # 選んだ行の各列について、すべての数字が同じ場合
    cnt = defaultdict(int)
    for j in range(W):
        val = P[target_h[0]][j]
        if all(P[i][j] == val for i in target_h):
            cnt[val] += 1

    if cnt.values():
        ans = max(ans, max(cnt.values()) * len(target_h))

print(ans)
