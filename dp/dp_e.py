N, W = map(int, input().split())

# wの範囲が広いため、vを使う
MAX_W = 10 ** 9 + 1
MAX_V = 1000 * N + 1
Baskets = [[MAX_W for i in range(MAX_V + 1)] for _ in range(N + 1)]
Baskets[0][0] = 0
# DPテーブルにはwを使う
# テーブルはそのvalueを満たす最小のwを求める
for i in range(1, N + 1):
    w, v = map(int, input().split())
    for j in range(MAX_V + 1):
        if j < v:
            Baskets[i][j] = Baskets[i - 1][j]
        else:
            Baskets[i][j] = min(Baskets[i - 1][j], Baskets[i - 1][j - v] + w)

# W以下の最大のvを求める
for i in reversed(range(MAX_V + 1)):
    if Baskets[N][i] <= W:
        print(i)
        break
