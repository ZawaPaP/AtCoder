N, W = map(int, input().split())

# 重さw, 価値vとして (w, v)
# それぞれ商品 i を入れた場合のv最大値と入れない場合のv最大値
Baskets = [[0 for i in range(W + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    w, v = map(int, input().split())
    for j in range(W + 1):
        if j < w:
            Baskets[i][j] = Baskets[i - 1][j]
        else:
            Baskets[i][j] = max(Baskets[i - 1][j], Baskets[i - 1][j - w] + v)

print(max(Baskets[N]))
